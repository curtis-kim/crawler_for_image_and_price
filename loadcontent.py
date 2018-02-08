# -*- coding: utf-8 -*-
import csv
import sys
import os
import urllib
import requests
import re
import savecontents
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
## This lib for Linux
from pyvirtualdisplay import Display

## create product-list csv
f = open("product-list.csv", "w")
writer = csv.writer(f)
writer.writerow(('name', 'price', 'special price', 'option name', 'option values', 'image list', 'content', 'source URL'))
## create img folder if it is not exist
path = "./img"
try:
    os.makedirs(path)
except OSError:
    if not os.path.isdir(path):
        raise
## read website list
f2 = open('website_list1.txt', "r")
website_list = f2.read().splitlines()

print website_list

## FUNCTION : Scraping HTML to list type
def parsingHtml():


    driver = webdriver.Chrome('./chromedriver')
    website_count = 0
    timeout = 5
    for i in website_list:
        ##driver.implicitly_wait(10)
	driver.get(i)

    
    element_present = EC.presence_of_element_located((By.CLASS_NAME, "tb-rmb-num"))
    WebDriverWait(driver, timeout).until(element_present)
    html[website_count] = driver.page_source
    return html


	
	##driver.implicitly_wait(10)
    

        ##driver.refresh()
    

## MAIN FUNCTION : write information to csv file
def main_function(html):
    for p in range(0, numofwebsite):
        soup = BeautifulSoup(html[p],"html.parser")
        information2 = savecontents.savefunction(soup)
        # information += website_list[p]
        information2.append(website_list[p])
        writer.writerow(information2)

    return




numofwebsite = len(website_list)
html = [0]*numofwebsite

## This line for Linux
display = Display(visible=0, size=(800, 800))
display.start()
###

main_function(parsingHtml())

#display.stop()

f.close()
