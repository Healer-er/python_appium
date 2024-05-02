import unittest
from time import sleep

from appium import webdriver
from selenium.webdriver.common.by import By


class AppiumTests_002(unittest.TestCase):
    def setUp(self):
        desired_caps = {
            "platformName": "Android",
            "platformVersion": "7.1.2",
            "deviceName": "huawei",
            "appPackage": "com.jiNing.feidao",
            "appActivity": ".ui.login.LoginActivity",
            "noReset": False
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities=desired_caps)
        self.driver.implicitly_wait(10)

    def tearDown(self):
        if self.driver:
            self.driver.quit()

    def test_example(self):
        self.driver.find_element(By.XPATH, '//*[@resource-id="com.jiNing.feidao:id/login_account_et"]').clear()
        self.driver.find_element(By.XPATH, '//*[@resource-id="com.jiNing.feidao:id/login_account_et"]').send_keys(
            'zhaofuxin')
        self.driver.find_element(By.XPATH, '//*[@resource-id="com.jiNing.feidao:id/login_pwd_et"]').clear()
        self.driver.find_element(By.XPATH, '//*[@resource-id="com.jiNing.feidao:id/login_pwd_et"]').send_keys(
            'Jifdl@2023')
        self.driver.find_element(By.XPATH, '//*[@resource-id="com.jiNing.feidao:id/login_btn"]').click()
        sleep(1.5)
        self.driver.save_screenshot(
            'C:\\Users\\admin\\Desktop\\workplace\\jnwxb\\jn_not_road\\picture\\login_page.png')
        sleep(1)
