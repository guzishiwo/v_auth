# -*- coding: utf-8 -*-
import json
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from random import choice
from taobao import api
from taobao.api import APP_KEY
from taobao.models import Token
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import urllib2
import logging
logger = logging.getLogger('taobao.views')


def gen_random_str(min_length=20, max_length=30, allowed_chars='abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789'):
        if min_length == max_length:
            length = min_length
        else:
            length = choice(range(min_length, max_length))
        return ''.join([choice(allowed_chars) for i in range(length)])


def auth(request):
    if request.method == "GET":
        _code = request.GET.get('code', None)
        # logger.info('Authorization grant {0}'.format(request.GET))
        try:
            rsp_parms = api.show_me(_code)
        except:
            logger.error('use code exchange access_code is failed')
            #  https://oauth.taobao.com/logoff?client_id=12304977&view=web）
            logger.error('Caused by {0}'.format(request.GET))
            logout_url = 'https://oauth.taobao.com/logoff'
            logger.debug(' start clean taobao cookies ')
            taobao_logout_url = '{0}?client_id={1}&view=web'.format(logout_url,
                                                                    APP_KEY)
            return HttpResponseRedirect(taobao_logout_url)

        taobao_user_nick = urllib2.unquote(rsp_parms.taobao_user_nick.encode('utf-8'))
        logger.info('taobao_user_nick = {0}'.format(taobao_user_nick))
        try:
            obj = Token.objects.get(taobao_user_nick=taobao_user_nick)
        except Token.DoesNotExist:
            logger.info('----------prepare create new record----------')
            obj = Token(
                access_token=rsp_parms.access_token,
                token_type=rsp_parms.token_type,
                expires_in=rsp_parms.expires_in,
                refresh_token=rsp_parms.refresh_token,
                re_expires_in=rsp_parms.get('re_expires_in', ''),
                r1_expires_in=rsp_parms.get('r1_expires_in', ''),
                r2_expires_in=rsp_parms.get('r2_expires_in', ''),
                w1_expires_in=rsp_parms.get('w1_expires_in', ''),
                w2_expires_in=rsp_parms.get('w2_expires_in', ''),
                taobao_user_id=rsp_parms.taobao_user_id,
                taobao_user_nick=taobao_user_nick,
                sub_taobao_user_nick=rsp_parms.get('sub_taobao_user_nick', ''),
                sub_taobao_user_id=rsp_parms.get('sub_taobao_user_id', ''))
            obj.save()
            logger.info('----------finish store new token ---------')
        else:
            logger.info('---------prepare update older token record-------')
            obj.access_token = rsp_parms.access_token
            obj.token_type = rsp_parms.token_type
            obj.expires_in = rsp_parms.expires_in
            obj.refresh_token = rsp_parms.refresh_token
            obj.re_expires_in = rsp_parms.get('re_expires_in', '')
            obj.r1_expires_in = rsp_parms.get('r1_expires_in', '')
            obj.r2_expires_in = rsp_parms.get('r2_expires_in', '')
            obj.w1_expires_in = rsp_parms.get('w1_expires_in', '')
            obj.w2_expires_in = rsp_parms.get('w2_expires_in', '')
            obj.taobao_user_id = rsp_parms.taobao_user_id
            obj.sub_taobao_user_nick = rsp_parms.get('sub_taobao_user_nick', '')
            obj.sub_taobao_user_id = rsp_parms.get('sub_taobao_user_id', '')
            obj.save()
            logger.info('----------finish update older token record-----------')

        url = 'http://www.vwms.cn/'
        # 跳转到网站的根目录，这里你可以设置授权成功后跳转uri
        return HttpResponseRedirect(url)


def login(request):
    url = api.get_authorize_url()
    logger.debug(url)
    next_url = request.META.get('HTTP_REFERER', None)
    if next_url:
        logger.info(next_url)
    return HttpResponseRedirect(url)


def query(request, nickname):
    if not request.user.is_authenticated():
        return HttpResponse(status=401)
    # nickname = urllib2.unquote(nickname.encode('utf-8'))
    try:
        obj = Token.objects.get(taobao_user_nick=nickname)
    except Token.DoesNotExist:
        logger.info('-------------query_failed ----------')
        return HttpResponse(status=404)
    else:
        response_data = dict(token_type=obj.token_type,
                             taobao_user_id=obj.taobao_user_id,
                             taobao_user_nick=obj.taobao_user_nick,
                             access_token=obj.access_token,
                             refresh_token=obj.refresh_token,
                             expires_in=obj.expires_in,
                             re_expires_in=obj.re_expires_in,
                             r1_expires_in=obj.r1_expires_in,
                             r2_expires_in=obj.r2_expires_in,
                             w1_expires_in=obj.w1_expires_in,
                             w2_expires_in=obj.w2_expires_in,
                             sub_taobao_user_nick=obj.sub_taobao_user_nick,
                             sub_taobao_user_id=obj.sub_taobao_user_id,)
        logger.info('--------- query_succeed --------')
        return HttpResponse(json.dumps(response_data),
                            content_type="application/json")
