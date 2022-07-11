#计时器函数，用于统计每个用例执行使用时间
import time
from dateutil.parser import parse
from selenium import webdriver


def setUp(self):
    self.browser = webdriver.Firefox()
    self.browser.set_window_size(1920, 1080)
    self.starttime = parse(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    print("开始测试时间：", self.starttime)
    # self.browser.get("http://oms-dev.romens.cloud:8087/")
    time.sleep(3)


# 结束函数，每个用例测试结束后，都会执行该函数
def tearDown(self):
    time.sleep(3)
    self.browser.quit()
    self.endtime = parse(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    print("测试结束时间：", self.endtime)
    totaltime = (self.endtime - self.starttime).total_seconds()
    print("总时长：", totaltime, "秒")