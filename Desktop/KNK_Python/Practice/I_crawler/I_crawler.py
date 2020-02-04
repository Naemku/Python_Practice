#!/usr/bin/env python
# coding: utf-8

# In[ ]:


search_keyword = str(input("*************************\n*************************\nType the Keyword: "))
search_number = int(input("*************************\n*************************\nHow many images do you want?: "))

if __name__ == '__main__':
    from icrawler.builtin import GoogleImageCrawler
    import time

    google_crawler = GoogleImageCrawler(storage={'root_dir':'C://Users//forma//Desktop//KNK_Python//Practice//Imagefolder'})
    time.sleep(1)
    print("*************************\n*************************\nCrawling and Downloading...Plz Wait...")
    google_crawler.crawl(keyword=search_keyword, max_num=search_number)
    time.sleep(1)
    print("*************************\n*************************\nCrawling Success!! Check your directory ('C://Users//forma//Desktop//KNK_Python//Practice//Imagefolder')")

