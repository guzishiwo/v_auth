from django.db import models
from marshmallow import Schema,fields, post_load

# Create your models here.
class JdToken(models.Model):
    access_token =  models.CharField(max_length=128, null=False)
    code = models.IntegerField(null=False)
    expires_in = models.IntegerField(null=False)
    refresh_token = models.CharField(max_length=128, null=False)
    scope = models.CharField(max_length=16, null=True)
    time = models.CharField(max_length=32, null=False)
    token_type = models.CharField(max_length=16, null=False)
    uid = models.CharField(max_length=128, null=False)
    user_nick = models.CharField(max_length=128, null=False)


class JdTokenSchema(Schema):

    class Meta:
        additional = ('access_token', 'code', 'expires_in', 'refresh_token',
                      'scope', 'time', 'token_type', 'uid', 'user_nick')