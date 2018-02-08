# -*- coding: utf-8 -*-
import urllib
import requests
import re
from time import gmtime, strftime

## Scraping From HTML Scripts
def savefunction(soup):
    information2 = []
    ####Find Name
    div = soup.find('div', attrs = {'id':"J_Title"})
    name = div.find('h3').get_text().encode('utf-8').replace(" ","")
    name = name.replace("\n","")
    information2.append(name)

    ####Find Price
    strong = soup.find('strong', attrs = {'id': "J_StrPrice"})
    price = strong.find("em", {"class":"tb-rmb-num"}).get_text().encode('utf-8')
    information2.append(price)

    ####Find special-price
    strong = soup.find('strong', attrs = {'class': "tb-promo-price"})
    special_price = strong.find("em", {"class":"tb-rmb-num"}).get_text().encode('utf-8')
    information2.append(special_price)

    ####Option Name
    dl = soup.find('dl', attrs = {'class': "J_Prop_Color"})
    option_name = dl.find("dt", {"class":"tb-property-type"}).get_text().encode('utf-8')
    information2.append(option_name)
    ####Option Value
    option_value = []
    for i in dl.find_all('a'):
        value=i.find('span').get_text().encode('utf-8')
        option_value.append(value)
    s = ", "
    option_value = s.join(option_value)
    information2.append(option_value)

    ####Image-List
    ul = soup.find('ul', attrs = {"id":'J_UlThumb'})
    url_count = 0
    image_list = []
    for j in ul.find_all('li'):
        inputTag = j.find('img')
        output = inputTag['data-src']
        url_count +=1

        rm_pattern = "_50x50.jpg"
        output = "https:" + re.sub(rm_pattern,'', output)


        image_name = "{}_00{}.jpg".format(strftime("%Y%m%d_%H%M%S", gmtime()), url_count)
        image_url = "./img/{}".format(image_name)
        urllib.urlretrieve(output, image_url)
        image_list.append(image_name)
        image_list_2 = s.join(image_list)
    information2.append(image_list_2)

    ####Description
    attributes_list = soup.find('ul', attrs = {'class':"attributes-list"})
    attributes_list = str(attributes_list)
    information2.append(attributes_list)
    ####print out

    #information = name + ", " + price + ", " + special_price + ", " + option_name + ", " + "\"" + option_value + "\"" + ", " + "\"" + image_list_2 + "\"" + ", " + "\"" + str(attributes_list) + "\"" + ", "

    return information2
