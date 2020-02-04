#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import openpyxl
import time

key_word = str(input("*************************\n*************************\nType your Searching key-word: "))
total_pages = int(input("*************************\n*************************\nHow many pages do you want to scrap?: "))
total_page = total_pages

if __name__ == "__main__":
    
#---Setting Chrome webdriver headless---
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('--disable-gpu')
    options.add_argument('lang=ko_KR')
#---------------------------------------

#---------------Making Excel file-----------------
    new_excel_file = openpyxl.Workbook()
    new_excel_sheet = new_excel_file.active
#-------------------------------------------------

#Executing Chrome Driver by locating its directory
    driver = webdriver.Chrome('C://Users//forma//Desktop//KNK_Python//Chromedriver_win32//chromedriver', options=options)

#Connecting Google by driver var.
    driver.get("https://google.com")

#Locating the input space by find_element_by_xpath
    search_location = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')

#---------------Making the title of sheet by key_word var-----------------
    new_excel_sheet.title = key_word
    new_excel_sheet.column_dimensions['A'].width = 66
    new_excel_sheet.column_dimensions['B'].width = 66
#-------------------------------------------------------------------------

#Searching Start
    search_location.send_keys(key_word)
    search_location.send_keys(Keys.ENTER)

    time.sleep(1)
    print("*************************\n*************************\nCrawling Start! Plz wait...")
    time.sleep(1)

#From here, loop all steps.
    while total_pages > 0:
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        data_set = soup.findAll('div', {'class':'r'})
        for i in data_set:
            link = i.find('a')
            title = i.find('h3')
            new_excel_sheet.append([title.get_text(), link.attrs['href']])
        #print(title.get_text(), "\n", link.attrs['href'])
        total_pages -= 1
        try:
            next_button = '//*[@id="pnnext"]/span[1]'
            next_button_location = driver.find_element_by_xpath(next_button)
            next_button_location.click()
        except:
            print('There are only {} pages in Google.'.format(total_page-total_pages))
            break
    #print("------------NEXT PAGE--------------")

    time.sleep(1)
    print('*************************\n*************************\nCrawling Success! Plz wait...')
    time.sleep(1)

#-------------Making column B in the excel file into hyperlink------------------
    for row_num, each_row in enumerate(new_excel_sheet.rows):
        new_excel_sheet.cell(row=row_num+1, column=2).hyperlink = each_row[1].value
#-------------------------------------------------------------------------------
    time.sleep(1)
    excel_file_name = str(input("*************************\n*************************\nType the name of excel file: "))
    time.sleep(1)
    new_excel_file.save('C://Users//forma//Desktop//KNK_Python//Practice//{}.xlsx'.format(excel_file_name))
    new_excel_file.close()
    time.sleep(1)
    print("*************************\n*************************\nSuccess! Check your file manually!!!")
    time.sleep(1)
    driver.quit()


# In[ ]:




