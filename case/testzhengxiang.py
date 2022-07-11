#正向流程测试用例

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from config import order_push
from config import order_state


def test_login():
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

    time.sleep(4)

    order_push.Order_push()
    time.sleep(7)

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
    # self.driver.find_element(By.CSS_SELECTOR,"el-scrollbar__view el-select-dropdown__list").click()
    # 13 | click | css=.hover |
    driver.find_element(By.XPATH, "/html/body/div[5]/div[1]/div[1]/ul/li[1]").click()
    # 14 | click | css=.picking-input:nth-child(2) .el-input__inner |
    driver.find_element(By.CSS_SELECTOR, ".picking-input:nth-child(2) .el-input__inner").click()
    # 15 | type | css=.picking-input:nth-child(2) .el-input__inner | 11111
    driver.find_element(By.CSS_SELECTOR, ".picking-input:nth-child(2) .el-input__inner").send_keys("11111")
    # 16 | click | css=.picking-input:nth-child(3) .el-input__inner |
    driver.find_element(By.CSS_SELECTOR, ".picking-input:nth-child(3) .el-input__inner").click()
    # 17 | type | css=.picking-input:nth-child(3) .el-input__inner | 11111
    driver.find_element(By.CSS_SELECTOR, ".picking-input:nth-child(3) .el-input__inner").send_keys("11111")
    # 18 | click | css=.el-button--success |
    driver.find_element(By.CSS_SELECTOR, ".el-button--success").click()
    # 19 | click | css=.el-button--default:nth-child(2) > span |
    driver.find_element(By.CSS_SELECTOR, ".el-button--default:nth-child(2) > span").click()
    time.sleep(1)
    # 20 | click | css=.el-button--success |
    driver.find_element(By.CSS_SELECTOR, ".el-button--success").click()
    # 21 | click | css=.el-button--default:nth-child(2) |
    driver.find_element(By.CSS_SELECTOR, ".el-button--default:nth-child(2)").click()
    # 22 | click | css=.el-button--primary:nth-child(1) |
    driver.find_element(By.CSS_SELECTOR, ".el-button--primary:nth-child(1)").click()
    time.sleep(1)
    order_state.Order_status()
    # 23 | click | css=.item-content:nth-child(3) span:nth-child(1) |
    driver.find_element(By.CSS_SELECTOR, ".item-content:nth-child(3) span:nth-child(1)").click()
    # 24 | click | css=.item-content:nth-child(5) span:nth-child(1) |
    driver.find_element(By.CSS_SELECTOR, ".item-content:nth-child(5) span:nth-child(1)").click()
    # 25 | click | css=.item-content:nth-child(6) span:nth-child(1) |
    driver.find_element(By.CSS_SELECTOR, ".item-content:nth-child(6) span:nth-child(1)").click()


if __name__ == '__main__':
    test_login()