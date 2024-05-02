import unittest
from time import sleep

from appium import webdriver
from selenium.webdriver.common.by import By


class AppiumTests_003(unittest.TestCase):
    def setUp(self):
        desired_caps = {
            "platformName": "Android",
            "platformVersion": "7.1.2",
            "deviceName": "huawei",
            "appPackage": "xdwl.example.com.intelligenturbanmanagement",
            "appActivity": "xdwl.example.com.login.login",
            "noReset": False
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities=desired_caps)
        self.driver.implicitly_wait(10)

    def tearDown(self):
        if self.driver:
            self.driver.quit()

    def test_example(self):
        # 登录页
        sleep(2)
        self.driver.save_screenshot(
            'C:\\Users\\admin\\Desktop\\workplace\\jnwxb\\learning_power\\picture\\login_page.png')
        self.driver.find_element(By.XPATH,
                                 '//*[@resource-id="xdwl.example.com.intelligenturbanmanagement:id/username"]').send_keys(
            'admin')
        self.driver.find_element(By.XPATH,
                                 '//*[@resource-id="xdwl.example.com.intelligenturbanmanagement:id/password"]').send_keys(
            '111111')
        self.driver.find_element(By.XPATH,
                                 '//*[@resource-id="xdwl.example.com.intelligenturbanmanagement:id/login"]').click()

        # 主页
        sleep(2)
        self.driver.save_screenshot(
            'C:\\Users\\admin\\Desktop\\workplace\\jnwxb\\learning_power\\picture\\main_page.png')

        # 工商管理
        self.driver.find_element(By.XPATH,'//*[@resource-id="xdwl.example.com.intelligenturbanmanagement:id/gdgl"]').click()
        sleep(2)
        self.driver.save_screenshot(
            'C:\\Users\\admin\\Desktop\\workplace\\jnwxb\\learning_power\\picture\\manage_page.png')
        sleep(1)
        self.driver.find_element(By.XPATH,'//*[@resource-id="xdwl.example.com.intelligenturbanmanagement:id/left_imgbt"]').click()

        # 数据展示
        self.driver.find_element(By.XPATH,'//*[@resource-id="xdwl.example.com.intelligenturbanmanagement:id/sjcj"]').click()
        sleep(15)
        self.driver.save_screenshot(
            'C:\\Users\\admin\\Desktop\\workplace\\jnwxb\\learning_power\\picture\\show_page.png')
        self.driver.find_element(By.XPATH,'//*[@resource-id="xdwl.example.com.intelligenturbanmanagement:id/left_imgbt"]').click()
        sleep(1)

        # 案件上报
        self.driver.find_element(By.XPATH,'//*[@resource-id="xdwl.example.com.intelligenturbanmanagement:id/sjsb"]').click()
        sleep(1)
        self.driver.save_screenshot(
            'C:\\Users\\admin\\Desktop\\workplace\\jnwxb\\learning_power\\picture\\case_page.png')
        self.driver.find_element(By.XPATH,'//*[@resource-id="xdwl.example.com.intelligenturbanmanagement:id/left_imgbt"]').click()
        sleep(2)

