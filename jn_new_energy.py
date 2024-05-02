import unittest
from time import sleep

from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class AppiumTests_001(unittest.TestCase):
    def setUp(self):
        desired_caps = {
            "platformName": "Android",
            "platformVersion": "7.1.2",
            "deviceName": "huawei",
            "appPackage": "dcdb.mingtu.com",  # 软件包
            "appActivity": "dcdb.mingtu.com.welcome.view.WelcomeView",  # 启动项
            "noReset": False
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities=desired_caps)
        self.driver.implicitly_wait(10)

    def tearDown(self):
        if self.driver:
            self.driver.quit()

    def test_example(self):
        # 滑动
        window_size = self.driver.get_window_size()
        x = window_size['width']
        y = window_size['height']
        for _ in range(3):
            self.driver.swipe(x * 0.9, y * 0.5, x * 0.2, y * 0.5, duration=100)
        try:
            self.driver.find_element(By.XPATH, '//*[@resource-id="dcdb.mingtu.com:id/btn_go_main"]').click()
            sleep(1)
        except NoSuchElementException:
            pass
        self.driver.find_element(By.XPATH, '//*[@resource-id="dcdb.mingtu.com:id/activity_login_username"]').clear()
        self.driver.find_element(By.XPATH, '//*[@resource-id="dcdb.mingtu.com:id/activity_login_username"]').send_keys(
            'sdzq')
        self.driver.find_element(By.XPATH, '//*[@resource-id="dcdb.mingtu.com:id/activity_login_password"]').clear()
        self.driver.find_element(By.XPATH, '//*[@resource-id="dcdb.mingtu.com:id/activity_login_password"]').send_keys(
            'Mingto&2022Ndx')
        self.driver.find_element(By.XPATH, '//*[@resource-id="dcdb.mingtu.com:id/activity_login_btn"]').click()
        sleep(1)
        self.driver.save_screenshot(
            'C:\\Users\\admin\\Desktop\\workplace\\jnwxb\\jn_new_energy\\picture\\login_page.png')
        sleep(1)
