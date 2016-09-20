#!/usr/bin/env python
#coding=utf-8

import mock
import requests
import unittest
from mock import patch
from selenium import webdriver
from django.http import HttpRequest
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "taobao.api")

class TaoBaoAuth(unittest.TestCase):

    def setUp(self):
        # self.browser = webdriver.Firefox()
        self.base_url = 'http://localhost:8000/'
        # self.browser.implicitly_wait(3)

    def tearDown(self):
        # self.browser.quit()
        pass

    # def test_auth2_for_taobao_server(self):
    #     home page
        # self.browser.get('http://localhost:8000')
        # assert 'page not found' in self.browser.title

    # def test_taobao_login_api(self):
    #     self.browser.get(self.base_url + 'login')
    #     assert u'淘宝购物' in self.browser.title


    @patch('taobao.api.show_me')
    def test_auth_can_save_information(self, my_param):
        my_param.return_value = ( 1,'guzi', '2YotnFZFEjr1zCsicMWpAA', 10 )
        r = requests.get(self.base_url + 'auth')



if __name__ == '__main__':
    unittest.main()
