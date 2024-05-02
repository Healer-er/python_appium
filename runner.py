# import unittest
#
# from app.jn_environment import AppiumTests_003
# from app.jn_not_road import AppiumTests_002
# from jn_new_energy import AppiumTests_001
#
#
# test_classes = [AppiumTests_001, AppiumTests_002,AppiumTests_003]
# test_suite = unittest.TestSuite([unittest.TestLoader().loadTestsFromTestCase(tc) for tc in test_classes])
# unittest.TextTestRunner(verbosity=2).run(test_suite)
from random import random

import requests


# 随机切换User-Agent：
# 在爬虫中报如下的错误：requests.exceptions.ConnectionError: (‘Connection aborted.’, RemoteDisconnected(‘Remote end closed connection without response’,))

user_agent_list = [
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15"
    ]


headers = {'User-Agent': random.choice(user_agent_list), 'Content-Type': 'application/json', 'method': 'GET',
           'Accept': 'application/vnd.github.cloak-preview'}

