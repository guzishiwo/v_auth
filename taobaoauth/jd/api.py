import os
from jd.utils.sdk import JdApiClinet
import logging
logger = logging.getLogger('taobao.views')

JD_APP_KEY = os.environ.get('JD_APP_KEY')
JD_APP_SECRET = os.environ.get('JD_APP_SECRET')
JD_CALLBACK_URL = os.environ.get('JD_CALLBACK_URL')


def get_authorize_url():
    try:
        client = JdApiClinet(app_key=JD_APP_KEY, app_secret=JD_APP_SECRET, redirect_uri=JD_CALLBACK_URL)
    except Exception,e:
        logger.error('JD Enviorment variable setting failed {0}'.format(e))
    return client.get_authorize_url()

def show_me(code):
    if code is None:
        logger.info('{0},{1}'.format('code is none', code))
    client = JdApiClinet(app_key=JD_APP_KEY, app_secret=JD_APP_SECRET, redirect_uri=JD_CALLBACK_URL)
    r = client.request_access_token(code)
    logger.info('JD success return access_token')
    return r

