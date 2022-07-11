#登陆函数封装
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def login():
    driver = webdriver.Firefox()
    driver.get("http://oms-dev.romens.cloud:8087/")
    time.sleep(0.5)
    driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/div[1]/input").send_keys("K001")
    time.sleep(0.5)
    driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/div[2]/input").send_keys("A123456")
    time.sleep(0.5)
    driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/button").click()
    time.sleep(2)
    driver.quit()

if __name__ == '__main__':
    login()