# from selenium import webdriver
# driver = webdriver.Chrome("./")
# driver.get("https://www.yahoo.co.jp/")
# driver.close()
# driver.quit()

# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

# ブラウザを開く。
driver = webdriver.Chrome()
# Googleの検索TOP画面を開く。
driver.get("https://www.smt-cinema.com/site/shinjuku/")
# 検索語として「selenium」と入力し、Enterキーを押す。
driver.find_element_by_id("0_1051_23745_20180311_2_77_0").click()
sleep(5)
driver.find_element_by_id("B-6-001-7-10-_").click()
# driver.find_element_by_id("lst-ib").send_keys(Keys.ENTER)
# タイトルに「Selenium - Web Browser Automation」が含まれるリンクをクリックする。
# driver.find_element_by_link_text("Selenium - Web Browser Automation").click()
# 5秒間待機してみる。
sleep(5)
# ブラウザを終了する。
driver.close()
driver.quit()
# document.getClassnameby("hoge").firstElementChild.click()