import unittest
from time import sleep

from appium import webdriver
from selenium.webdriver.common.by import By


class AppiumTests_004(unittest.TestCase):
    def setUp(self):
        desired_caps = {
            "platformName": "Android",
            "platformVersion": "12",
            "deviceName": "huawei",
            "appPackage": "tv.suosi.sdedunews",
            "appActivity": "io.dcloud.PandoraEntry",
            "noReset": False
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities=desired_caps)
        self.driver.implicitly_wait(10)

    def tearDown(self):
        if self.driver:
            self.driver.quit()

    def test_example(self):
        sleep(2)
        self.driver.save_screenshot(
            'picture\\first_page.png')
        self.driver.find_element(By.XPATH, '//*[@resource-id="tv.suosi.sdedunews:id/btn_custom_privacy_sure"]').click()
        sleep(4)
        self.driver.save_screenshot(
            'picture\\news_page.png')
        self.driver.find_element(By.XPATH,
                                 '//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]').click()
        sleep(6)
        self.driver.save_screenshot(
            'picture\\videos_page.png')

        self.driver.find_element(By.XPATH,
                                 '//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[3]').click()
        sleep(2)
        self.driver.save_screenshot(
            'picture\\edu_page.png')

        self.driver.find_element(By.XPATH,
                                 '//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[4]').click()
        sleep(2)
        self.driver.save_screenshot(
            'picture\\my_page.png')
        sleep(1)
