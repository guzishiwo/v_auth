#!/usr/bin/env python
#coding=utf-8
import mock
import json
from mock import patch
from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from taobao.views import login,auth,query
from taobao.models import Token
from taobao.utils.sdk import APIClient,_parse_json


class TestTaoBaoThirdLogin(TestCase):
    # Test api /login/  and /auth/
    def test_taobao_url_resolve_login_and_auth_view(self):
        found = resolve('/login/')
        self.assertEqual(found.func, login)
        found = resolve('/auth/')
        self.assertEqual(found.func, auth)

    @patch("taobao.api.show_me")
    def test_auth_api_get_access_token_param_by_nickname_english(self, access_token):
        token_param = dict(
            taobao_user_id=263685215,
            taobao_user_nick='guzishiwo',
            w1_expires_in=1800,
            re_expires_in=0,
            r2_expires_in=0,
            expires_in=86400,
            token_type="Bearer",
            refresh_token="6200e1909ca29b04685c49d67f5ZZ3675347c0c6d5abccd263685215",
            access_token="6200819d9366af1383023a19907ZZf9048e4c14fd56333b263685215",
            r1_expires_in=1800
        )
        json_dict = json.dumps(token_param)
        access_token.return_value = _parse_json(json_dict)
        request = HttpRequest()
        request.method = 'GET'
        response = auth(request)
        save_tokens = Token.objects.all()
        self.assertEqual(save_tokens.count(), 1)

    @patch("taobao.api.show_me")
    def test_auth_api_get_access_token_param_by_nickname_chinese(self, access_token):
        token_param = dict(
            taobao_user_id=263685215,
            taobao_user_nick=u'中文',
            w1_expires_in=1800,
            re_expires_in=0,
            r2_expires_in=0,
            expires_in=86400,
            token_type="Bearer",
            refresh_token="6200e1909ca29b04685c49d67f5ZZ3675347c0c6d5abccd263685215",
            access_token="6200819d9366af1383023a19907ZZf9048e4c14fd56333b263685215",
            r1_expires_in=1800
        )
        json_dict = json.dumps(token_param)
        access_token.return_value = _parse_json(json_dict)
        request = HttpRequest()
        request.method = 'GET'
        response = auth(request)
        save_tokens = Token.objects.all()
        self.assertEqual(save_tokens.count(), 1)

class ItemModelTest(TestCase):

    def test_insert_data_in_taobao_token(self):
        first_token = Token.objects.create(
            token_type='Bearer',
            expires_in=10,
            re_expires_in = 10,
            refresh_token='2YotnFZFEjr1zCsicMWpAA',
            taobao_user_id=123456,
            r1_expires_in=10,
            r2_expires_in=10,
            w1_expires_in=10,
            w2_expires_in=10,
            access_token='aaaiij',
            taobao_user_nick='guzi',
            sub_taobao_user_nick='',
        )
        save_tokens = Token.objects.all()
        self.assertEqual(save_tokens.count(), 1)
        find_obj = Token.objects.filter(taobao_user_id = 123456).first()
        self.assertEqual(first_token, find_obj)

