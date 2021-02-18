from selenium import webdriver
import time
import csv
import os.path
from time import gmtime, strftime
from datetime import datetime

def GenerateReport(query):
    # path of chrome driver
    driver = webdriver.Chrome (executable_path="/home/himani/Documents/python-webui-testing/tests/chrome/chromedriver_linux64 (2)/chromedriver")
    driver.maximize_window()
    # get url
    driver.get("https://www.bing.com/search")
    driver.maximize_window()

    # input one plus 8 in search field
    driver.find_element_by_xpath('//input[@id="sb_form_q"]').send_keys(query) 
    time.sleep(12)

    # click on search button
    driver.find_element_by_xpath('//body/div[2]/div[1]/div[3]/div[2]/form[1]/label[1]/*[1]').click()

    # get list of all links
    lnks=driver.find_elements_by_tag_name("cite")
    Links = []
    for links in lnks:
        link_name = links.text
        Links.append(link_name)


    #  get list of all title name in seach result
    title_name = driver.find_elements_by_partial_link_text('OnePlus 8')
    texts = []
    for title in title_name:
        text = title.text
        texts.append(text)


    # get list of all contents 
    details = driver.find_elements_by_tag_name('p')
    Search_details = []
    for content in details:
        contents = content.text
        Search_details.append(contents)

    # export data to csv
    headers = ['LINKS', 'TITLE','DESCRIPTION']

    with open('finalData.csv', 'a') as f:
        file_is_empty = os.stat('finalData.csv').st_size == 0
        writer = csv.writer(f)
        if file_is_empty:
            writer.writerow(headers)
        writer.writerows(zip(Links, texts, Search_details))

            
    driver.quit()



#Calling above func

GenerateReport("onePlus8")