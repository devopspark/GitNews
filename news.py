from bs4 import BeautifulSoup as bs
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options = options)
driver.get("https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EC%86%8D%EB%B3%B4")
time.sleep(1)
titleList = []

for i in range(20):
    body = driver.find_element(By.CSS_SELECTOR, "body")
    body.send_keys(Keys.END)
    time.sleep(1)

soup = bs(driver.page_source,"lxml")
title = soup.select("a.news_tit")

for i in title:
    titleList.append(i.text)

dic = {"속보제목" : titleList}
df = pd.DataFrame(dic)
df.to_csv("속보data.csv", encoding = "utf-8-sig", index=False)
