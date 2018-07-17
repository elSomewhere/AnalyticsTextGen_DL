import requests
from bs4 import BeautifulSoup
import os
#os.chdir('~/crawl')

from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.common.by import By
opts = FirefoxOptions()
opts.add_argument("--headless")
browser = webdriver.Firefox(firefox_options=opts)
#browser = webdriver.Firefox()
browser.get(("https://investment.credit-suisse.com/Search/Start?start=1&PageContext=ArticleSearch"))
html_source = browser.page_source


browser.find_element_by_xpath("//select[@id='DomicilePoolpartyConceptId']/option[@value='http://poolpartyw.csintra.net/SolutionNetThesaurus/Switzerland']").click()
browser.find_element_by_xpath("//select[@id='UiLanguagePoolpartyConceptId']/option[@value='http://poolpartyw.csintra.net/SolutionNetThesaurus/English']").click()
browser.find_element_by_id('loginButton').click()

globalCount = 0
count = 0
url = browser.current_url


current = url



while True:
    print(browser.current_url)
    links = []
    sources = []
    for url in browser.find_elements_by_xpath('//a[starts-with(@href, "/Article")]'):
        article = url.get_attribute('href')
        links.append(article)   
    for url in links:
        browser.get(url)
        print(browser.current_url)
        content = browser.page_source
        sources.append(content)
        text_file = open(os.path.join("~/crawl/rawDat",str(globalCount)+"_Output.txt"), "w")
        text_file.write(content)
        text_file.close()
        print(globalCount)
        globalCount = globalCount + 1
    browser.get(current)
    count = count + 25
    current = 'https://investment.credit-suisse.com/Search/Start?start=%s&PageContext=ArticleSearch' % (count)
    
    




