# coding=utf-8
from django.db import models


class Token(models.Model):
    token_type = models.CharField(max_length=32, null=False)
    access_token =  models.CharField(max_length=128, null=False)
    refresh_token = models.CharField(max_length=128, null=False)
    expires_in =    models.CharField(max_length=64, null=False)
    re_expires_in = models.CharField(max_length=32, null=False)
    r1_expires_in = models.CharField(max_length=32, null=False)
    r2_expires_in = models.CharField(max_length=32, null=False)
    w1_expires_in = models.CharField(max_length=32, null=False)
    w2_expires_in = models.CharField(max_length=32, null=False)
    taobao_user_id = models.CharField(max_length=64, null=False)
    taobao_user_nick = models.CharField(max_length=128, null=False)
    sub_taobao_user_nick = models.CharField(max_length=64, null=True)
    sub_taobao_user_id = models.CharField(max_length=32, null=True)
    created_time = models.DateTimeField(auto_now_add=True,
                                        editable=False, db_index=True)
    updated_time = models.DateTimeField(auto_now=True,
                                        editable=False, db_index=True)

    def __unicode__(self):
        return self.taobao_user_nick
