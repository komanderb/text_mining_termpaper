# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 13:43:08 2022
Scraping children books
"""
# Loading relevant packages ===================================================
import matplotlib
import camelot
import os
import pandas as pd
import lxml
from functools import reduce
from time import sleep
import selenium
from selenium import webdriver
#pip install webdriver-manager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 
warnings.filterwarnings('ignore', category=UserWarning)


# First URL ===================================================================
# This scraper is going to be so messy because I couldn't loop as otherwise chrome 
# would not be reachable
url = 'https://www.gutenberg.org/ebooks/bookshelf/216'

def id_scraper(link): 
    # this scraper might not be ideal but the webpage is rather confusing
    # also this is going to be super cautious
    link_list = []
    id_list = []
    download_data = []
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(url)
    results = browser.find_element_by_xpath('//*[@id="content"]/div[2]/div/ul')
    book_list = results.find_elements_by_class_name('booklink')
    for counter, item in enumerate(book_list):
        link_list.append(book_list[counter].find_element_by_class_name('link').get_attribute('href'))
    #link_list = list_maker(link_list)
    sleep(0.5)
    browser.find_element_by_xpath('//*[@id="content"]/div[2]/div/ul/li[3]/div/span[2]/a').click()
    sleep(2)
    results = browser.find_element_by_xpath('//*[@id="content"]/div[2]/div/ul')
    book_list = results.find_elements_by_class_name('booklink')
    for counter, item in enumerate(book_list):
        link_list.append(book_list[counter].find_element_by_class_name('link').get_attribute('href'))
    #link_list = list_maker(link_list)
    # and next page
    browser.find_element_by_xpath('//*[@id="content"]/div[2]/div/ul/li[1]/div/span[2]/a[3]').click()
    sleep(0.5)
    results = browser.find_element_by_xpath('//*[@id="content"]/div[2]/div/ul')
    book_list = results.find_elements_by_class_name('booklink')
    for counter, item in enumerate(book_list):
        link_list.append(book_list[counter].find_element_by_class_name('link').get_attribute('href'))
    #link_list = list_maker(link_list)
    
    sleep(1)
    for counter, link in enumerate(link_list):
        sleep(0.5)
        browser.get(link)
        sleep(1)
        table = browser.find_element_by_xpath('//*[@id="bibrec"]/div/table')
        list_th = table.find_elements_by_tag_name('th')
        list_td = table.find_elements_by_tag_name('td')
        for counter, item in enumerate(list_th):
            if list_th[counter].text == 'EBook-No.' :
                id_list.append(list_td[counter].text)
            elif list_th[counter].text == 'Downloads':
                download_data.append(list_td[counter].text)
            else: 
                pass
        
    
    return(id_list, download_data)
    
    
list_id, dl_data = id_scraper(url)
# write the data
os.chdir(r"C:\Users\lenovo\Documents\GitHub\text_mining_termpaper\data")

    
fairy_tailes = pd.DataFrame(
    {'book_id': list_id,
     'download_data': dl_data})
fairy_tailes.to_csv('fairy_id.csv')
