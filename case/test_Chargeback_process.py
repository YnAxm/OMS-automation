#退单流程用例
# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from config import tuidandingdan


def Test_tuidan():
    tuidandingdan.Order_tuidan()
    time.sleep(2)
    driver = webdriver.Firefox()
    driver.maximize_window()
    #     self.driver.set_window_size(1920, 1080)
    driver.get("http://oms-dev.romens.cloud:8087/")
    driver.set_window_size(1936, 1056)
    driver.find_element(By.CSS_SELECTOR, ".el-input:nth-child(1) > .el-input__inner").send_keys("K001")
    driver.find_element(By.CSS_SELECTOR, ".login-input-bottom > .el-input__inner").send_keys("A123456")
    driver.find_element(By.CSS_SELECTOR, ".el-button").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, ".item-content:nth-child(9) span:nth-child(1)").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, ".el-radio-button:nth-child(2) > .el-radio-button__inner").click()
    driver.find_element(By.CSS_SELECTOR, ".etails").click()
    driver.find_element(By.CSS_SELECTOR, ".btn-print").click()
    time.sleep(1)
    driver.find_element_by_xpath('//button[@class="el-button el-button--default el-button--small el-button--primary "]').click()
    #切换回未处理页面
    time.sleep(3)
    driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/section/main/div/div/div[1]/div/div[1]/div/div[2]/div[1]/div/label[2]/span").click()
    driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/section/main/div/div/div[2]/div[1]/div[1]/div/div/div[2]/div/div/input").send_keys("010102")
    time.sleep(2)
    driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/section/main/div/div/div[2]/div[1]/div[1]/div/div/div[1]/div[2]/div/div/button").click()
    driver.find_element_by_xpath('//button[@class="el-button el-button--default el-button--small el-button--primary "]').click()

if __name__ == '__main__':
    Test_tuidan()