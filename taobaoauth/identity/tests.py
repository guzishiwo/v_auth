import json
from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.utils.encoding import force_text
from identity.views import auth_login, auth_logout
from django.contrib.auth.models import User
# Create your tests here.

class AuthState(TestCase):

    def test_auth_login_url_resolves_to_my_view(self):
        found = resolve('/identity/login')
        self.assertEqual(found.func, auth_login)

    def test_auth_logout_url_resolves_to_my_view(self):
        found = resolve('/identity/logout')
        self.assertEqual(found.func, auth_logout)

    def test_auth_no_header_login_failed_return_data(self):
        content={
            'username':'Vwms',
            'password':'vwms'
        }
        response = self.client.post('/identity/login',
                                    json.dumps(content),
                                    content_type='application/json',
                                    )
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            force_text(response.content),
            {"login": "invalid login !"}
        )

    def test_auth_username_errors_login_return_data(self):
        content={
            'username':'Vs',
            'password':'vwms'
        }
        response = self.client.post('/identity/login',
                                    json.dumps(content),
                                    content_type='application/json',
                                    HTTP_TOKEN='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwYXNzd29yZCI6InZ3bXMiLCJ1c2VybmFtZSI6IlZ3bXMifQ.GP497LDUSHq-WwPw3eKcm68joexEz_NFI3ZASo6jomA'
                                    )
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            force_text(response.content),
            {"login": "invalid login"}
        )

    def test_auth_correct_login_return_correct_data(self):
        user = User.objects.create_user('Vwms', '@v.com', 'vwms')
        content={
            'username':'Vwms',
            'password':'vwms'
        }
        response = self.client.post('/identity/login',
                                    json.dumps(content),
                                    content_type='application/json',
                                    HTTP_TOKEN='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwYXNzd29yZCI6InZ3bXMiLCJ1c2VybmFtZSI6IlZ3bXMifQ.GP497LDUSHq-WwPw3eKcm68joexEz_NFI3ZASo6jomA'
                                    )
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            force_text(response.content),
            {"login": "success"}
        )

    def test_auth_login_visit_success_vist_view(self):
        user = User.objects.create_user('Vwms', '@v.com', 'vwms')
        content={
            'username':'Vwms',
            'password':'vwms'
        }
        response = self.client.post('/identity/login',
                                    json.dumps(content),
                                    content_type='application/json',
                                    HTTP_TOKEN='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwYXNzd29yZCI6InZ3bXMiLCJ1c2VybmFtZSI6IlZ3bXMifQ.GP497LDUSHq-WwPw3eKcm68joexEz_NFI3ZASo6jomA'
                                    )
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            force_text(response.content),
            {"login": "success"}
        )
        response = self.client.get('/query/guzi')
        self.assertEqual(response.status_code, 404)




    # def test_auth_login_correct_return_data1(self):
    #     request = HttpRequest()
    #     request.method = "POST"
    #
    #     request.META.

