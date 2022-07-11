#自提订单流程

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from config import Self_delivery_order

def test_zitidingdan():
    # Test name: 登陆
    # Step # | name | target | value
    driver = webdriver.Firefox()
    driver.set_window_size(1920, 1080)
    # 1 | open | / |
    driver.get("http://oms-dev.romens.cloud:8087/")
    # 3 | click | css=.el-input:nth-child(1) > .el-input__inner |
    driver.find_element(By.CSS_SELECTOR, ".el-input:nth-child(1) > .el-input__inner").click()
    # 4 | type | css=.el-input:nth-child(1) > .el-input__inner | K001
    driver.find_element(By.CSS_SELECTOR, ".el-input:nth-child(1) > .el-input__inner").send_keys("K001")
    # 5 | click | css=.login-input-bottom > .el-input__inner |
    driver.find_element(By.CSS_SELECTOR, ".login-input-bottom > .el-input__inner").click()
    # 6 | type | css=.login-input-bottom > .el-input__inner | A123456
    driver.find_element(By.CSS_SELECTOR, ".login-input-bottom > .el-input__inner").send_keys("A123456")
    # 7 | click | css=.el-button |
    driver.find_element(By.CSS_SELECTOR, ".el-button").click()
    time.sleep(3)  # 页面静止三秒进行订单推送
    Self_delivery_order.Order_Self_withdrawal_push()
    time.sleep(3)  # 订单推送完成，等待3秒
    # 8 | click | css=.item-content:nth-child(2) span:nth-child(2) |
    driver.find_element(By.CSS_SELECTOR, ".item-content:nth-child(2) span:nth-child(2)").click()
    time.sleep(2)
    # 9 | click | css=.el-button--success |
    driver.find_element(By.CSS_SELECTOR, ".el-button--success").click()
    # 10 | click | css=.el-button--default:nth-child(2) |
    driver.find_element(By.CSS_SELECTOR, ".el-button--default:nth-child(2)").click()
    # 11 | click | css=.item-content:nth-child(3) span:nth-child(1) |
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, ".item-content:nth-child(3) span:nth-child(1)").click()
    # 12 | click | css=.el-input--suffix:nth-child(1) > .el-input__inner |
    driver.find_element(By.CSS_SELECTOR, ".el-input--suffix:nth-child(1) > .el-input__inner").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, ".picking-input > .el-input > .el-input__inner").send_keys("111111")
    # 15 | click | css=.el-button--success |
    driver.find_element(By.CSS_SELECTOR, ".el-button--success").click()
    driver.find_element(By.CSS_SELECTOR, ".el-button--default:nth-child(2)").click()
    time.sleep(2)
    # 以上代码已完成拣货操作
    driver.find_element(By.XPATH, "/html/body/div/div/div[2]/section/aside/div[2]/div[8]").click()  # 单击“上门自提“订单状态栏
    time.sleep(1)  # 流出页面刷新时间
    driver.find_element(By.XPATH, "/html/body/div/div/div[2]/section/main/div/div/div[1]/div/div[2]/div[1]").click()  # 单击门店自提状态第一个订单
    driver.find_element(By.XPATH,"/html/body/div/div/div[2]/section/main/div/div/div[2]/div/div[1]/div/div/div[2]/div/div/input").send_keys("111111")  # 定位自提码输入框，并输入自提码-1111111
    driver.find_element(By.XPATH,"/html/body/div/div/div[2]/section/main/div/div/div[2]/div/div[1]/div/div/div[1]/div[2]/div/button[2]").click()  # 定位自提输入框
    driver.find_element_by_xpath('//button[@class="el-button el-button--default el-button--small el-button--primary "]').click()


if __name__ == '__main__':
    test_zitidingdan()