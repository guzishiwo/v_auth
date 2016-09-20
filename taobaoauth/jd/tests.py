#!/usr/bin/env python
#coding=utf-8
import mock
import json
from mock import patch
from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
import api
from jd.views import jd_login,jd_auth,jd_query
from jd.models import JdToken
from taobao.utils.sdk import APIClient,_parse_json


class TestjdThirdLogin(TestCase):
    # Test api /login/  and /auth/
    def test_jd_url_resolve_login_and_auth_view(self):
        found = resolve('/jd/login/')
        self.assertEqual(found.func, jd_login)
        found = resolve('/jd/auth/')
        self.assertEqual(found.func, jd_auth)

    @patch("jd.api.show_me")
    def test_auth_api_get_access_token_param_by_nickname_english(self, access_token):
        token_param = dict(
            access_token='aaaiij',
            code = 0,
            expires_in=10,
            refresh_token='2YotnFZFEjr1zCsicMWpAA',
            time="12349924343",
            token_type='Bearer',
            uid="1234",
            user_nick="1234567",
        )
        json_dict = json.dumps(token_param)
        access_token.return_value = _parse_json(json_dict)
        request = HttpRequest()
        request.method = 'GET'
        response = jd_auth(request)
        save_tokens = JdToken.objects.all()
        self.assertEqual(save_tokens.count(), 1)

    @patch("jd.api.show_me")
    def test_auth_api_get_access_token_param_by_nickname_chinese(self, access_token):
        token_param = dict(
            access_token='aaaiij',
            code = 0,
            expires_in=10,
            refresh_token='2YotnFZFEjr1zCsicMWpAA',
            time="12349924343",
            token_type='Bearer',
            uid="1234",
            user_nick="王大锤",
        )
        json_dict = json.dumps(token_param)
        access_token.return_value = _parse_json(json_dict)
        request = HttpRequest()
        request.method = 'GET'
        response = jd_auth(request)
        save_tokens = JdToken.objects.all()
        self.assertEqual(save_tokens.count(), 1)


class JDModelTest(TestCase):

    def test_insert_data_in_jd_token(self):
        first_token = JdToken.objects.create(
            access_token='aaaiij',
            code = 0,
            expires_in=10,
            refresh_token='2YotnFZFEjr1zCsicMWpAA',
            time="12349924343",
            token_type='Bearer',
            uid="1234",
            user_nick="1234567",
        )
        save_tokens = JdToken.objects.all()
        self.assertEqual(save_tokens.count(), 1)
        find_obj = JdToken.objects.filter(user_nick="1234567").first()
        self.assertEqual(first_token, find_obj)
