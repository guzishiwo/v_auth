#coding=utf-8
import jwt
import json
from django.shortcuts import render, HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
# Create your views here.

@require_http_methods(["POST"])
def auth_login(request):
    http_token = request.META.get('HTTP_TOKEN',False)
    http_body = request.body
    if not http_token:
        return JsonResponse({'login':'invalid login !'})
    # header 验证
    header_data = jwt.decode(http_token, 'secret', algorithms=['HS256'])
    header_username = header_data.get('username', False)
    header_password = header_data.get('password', False)
    header_user = authenticate(username=header_username, password=header_password)
    # body 验证数据
    body_data = json.loads(http_body)
    body_username = body_data.get('username', False)
    body_password = body_data.get('password', False)
    body_user = authenticate(username=body_username, password=body_password)
    if body_user == header_user:
        if header_user is not None:
            if header_user.is_active:
                login(request, header_user)
                # print 'success'
                return JsonResponse({'login':'success'})
            else:
                # Return a 'disabled account' error message
                return JsonResponse({'login':'disabled account'})
        else:
            # Return an 'invalid login' error message.
            return JsonResponse({'login':'invalid login'})
    else:
        return  JsonResponse({'login': 'failed'})


def auth_logout(request):
    logout(request)
    return JsonResponse({'logout':'success'})
