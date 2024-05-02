import unittest
from time import sleep

from appium import webdriver
from selenium.webdriver.common.by import By
import uiautomator2 as u2


class AppiumTests_003(unittest.TestCase):
    def setUp(self):
        self.devices = u2.connect()
        self.devices.app_clear('com.jnzhhb.clgk')
        self.devices.app_start('com.jnzhhb.clgk', wait=True)
        self.devices.wait_timeout = 10

    def tearDown(self):
        self.devices.app_stop('com.jnzhhb.clgk')
        self.devices.app_clear('com.jnzhhb.clgk')

    def test_example(self):
        self.devices(text='同意').click()
        sleep(1.5)
        self.devices.screenshot(r'C:\\Users\\admin\\Desktop\\workplace\\jnwxb\\jn_environment\\picture\\login_page.png')
        sleep(1.5)

        self.devices(resourceId='com.jnzhhb.clgk:id/username', text='请输入用户名').send_keys('hbj')
        # self.devices(text='请输入密码').click()
        # self.devices.press('delete')
        self.devices(resourceId='com.jnzhhb.clgk:id/password', text='请输入密码').send_keys('hik12345++')
        sleep(1)
        self.devices(text='60.211.166.115:1443').clear_text()
        sleep(1)
        self.devices(text='请输入服务器地址').send_keys('182.45.132.62:1443')
        sleep(1)
        self.devices.xpath('//*[@resource-id="com.jnzhhb.clgk:id/log_in_button"]').click()
        sleep(2)
        self.devices.screenshot(r'C:\\Users\\admin\\Desktop\\workplace\\jnwxb\\jn_environment\\picture\\home_page.png')
        sleep(2)
        # 车辆管控
        self.devices.click(101, 1555)
        sleep(100)
        self.devices.screenshot(
            r'C:\\Users\\admin\\Desktop\\workplace\\jnwxb\\jn_environment\\picture\\car_control_page.png')
        self.devices.click(265, 244)
        sleep(1)
        self.devices.screenshot(
            r'C:\\Users\\admin\\Desktop\\workplace\\jnwxb\\jn_environment\\picture\\car_control_01_page.png')
        self.devices.click(36, 68)
        sleep(1)

        # 待办事项
        self.devices.click(297, 1563)
        sleep(1)
        self.devices.screenshot(
            r'C:\\Users\\admin\\Desktop\\workplace\\jnwxb\\jn_environment\\picture\\unresolved_control_01_page.png')
        self.devices.click(673, 65)
        sleep(1)
        self.devices.screenshot(
            r'C:\\Users\\admin\\Desktop\\workplace\\jnwxb\\jn_environment\\picture\\unresolved_control_02_page.png')

        # 企业信息
        self.devices.click(600, 1558)
        sleep(1)
        self.devices.screenshot(
            r'C:\\Users\\admin\\Desktop\\workplace\\jnwxb\\jn_environment\\picture\\enterprise_page.png')
        self.devices.click(326, 262)
        sleep(1)
        self.devices.screenshot(
            r'C:\\Users\\admin\\Desktop\\workplace\\jnwxb\\jn_environment\\picture\\enterprise_01_page.png')
        # 返回
        self.devices.click(36, 68)

        # 辅助查询
        self.devices.click(795, 1550)
        sleep(1)
        self.devices.screenshot(
            r'C:\\Users\\admin\\Desktop\\workplace\\jnwxb\\jn_environment\\picture\\query_page.png')
        sleep(1)
