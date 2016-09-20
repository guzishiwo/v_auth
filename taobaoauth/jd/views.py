# -*- coding: utf-8 -*-
import json
import logging
import urllib2
from jd import api
from jd.models import JdToken
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from jd.models import JdTokenSchema
logger = logging.getLogger('taobao.views')


def jd_auth(request):
    if request.method == "GET":
        _code = request.GET.get('code', None)
        try:
            rsp_parms = api.show_me(_code)
        except:
            logger.error('use code exchange access_code is failed')
            logger.error('Caused by {0}'.format(request.GET))
        jd_user_nick = urllib2.unquote(rsp_parms.user_nick.encode('utf-8'))
        logger.info('jd_user_nick = {0}'.format(jd_user_nick))
        logger.info('JD_token {0}'.format(rsp_parms))
        try:
            obj = JdToken.objects.get(user_nick=jd_user_nick)
        except JdToken.DoesNotExist:
            logger.info('----------JD prepare create new record----------')
            obj = JdToken(
                access_token=rsp_parms.access_token,
                code=rsp_parms.code,
                expires_in=rsp_parms.expires_in,
                refresh_token=rsp_parms.refresh_token,
                time=rsp_parms.time,
                token_type=rsp_parms.token_type,
                uid=rsp_parms.uid,
                user_nick=rsp_parms.user_nick
            )
            obj.save()
            logger.info('----------JD finish store new token ---------')
        else:
            logger.info('---------JD prepare update older token record-------')
            obj = JdToken(
                access_token=rsp_parms.access_token,
                code=rsp_parms.code,
                expires_in=rsp_parms.expires_in,
                refresh_token=rsp_parms.refresh_token,
                scope=rsp_parms.scope,
                time=rsp_parms.time,
                token_type=rsp_parms.token_type,
                uid=rsp_parms.uid,
            )
            obj.save()
            logger.info('----------JD finish update older token record-----------')
        url = 'http://www.vwms.cn/'
        return HttpResponseRedirect(url)

def jd_login(request):
    url = api.get_authorize_url()
    logger.debug(url)
    next_url = request.META.get('HTTP_REFERER', None)
    if next_url:
        logger.info(next_url)
    return HttpResponseRedirect(url)


def jd_query(request, nickname):
    if not request.user.is_authenticated():
        return HttpResponse(status=401)
    try:
        jd_obj = JdToken.objects.get(taobao_user_nick=nickname)
    except JdToken.DoesNotExist:
        logger.info('-------------jd query_failed ----------')
        return HttpResponse(status=404)
    else:
        jd_data = JdTokenSchema().dumps(jd_obj)
        logger.info('---------jd query_succeed --------')
        return HttpResponse(jd_data, content_type="application/json")
