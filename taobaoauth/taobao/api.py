import os
from django.conf import settings
from taobao.utils.sdk import APIClient
import logging
logger = logging.getLogger('taobao.views')

APP_KEY = os.environ.get('TAOBAO_APP_KEY')
APP_SECRET = os.environ.get('TAOBAO_APP_SECRET')
CALLBACK_URL = os.environ.get('TAOBAOCALLBACK_URL')


def get_authorize_url():
    try:
        client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
    except Exception,e:
        logger.error('Enviorment variable setting failed {0}'.format(e))
    return client.get_authorize_url()


def show_me(code):
    if code is None:
        logger.info('{0},{1}'.format('code is none', code))
    client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
    r = client.request_access_token(code)
    logger.info('taobao success return access_token')
    return r

def unbind(access_token):
    if access_token is None:
        raise Exception('access token None')
    client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
    # client.set_access_token(access_token, expires_in)
    return client.request_revoke(access_token)
    # return client.revokeoauth2.get()
