from taobao.utils.sdk import APIClient


class JdApiClinet(APIClient):

    def __init__(self, app_key, app_secret, redirect_uri=None, response_type='code', domain='oauth.jd.com/oauth', version='2'):
        super(JdApiClinet, self).__init__(app_key, app_secret, redirect_uri, response_type, domain, version)
        self.auth_url = 'https://oauth.jd.com/oauth/authorize'
        self.token_url = 'https://oauth.jd.com/oauth/token'


