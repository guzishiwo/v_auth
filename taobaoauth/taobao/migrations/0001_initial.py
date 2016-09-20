# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('token_type', models.CharField(max_length=32)),
                ('access_token', models.CharField(max_length=128)),
                ('refresh_token', models.CharField(max_length=128)),
                ('expires_in', models.CharField(max_length=64)),
                ('re_expires_in', models.CharField(max_length=32)),
                ('r1_expires_in', models.CharField(max_length=32)),
                ('r2_expires_in', models.CharField(max_length=32)),
                ('w1_expires_in', models.CharField(max_length=32)),
                ('w2_expires_in', models.CharField(max_length=32)),
                ('taobao_user_id', models.CharField(max_length=64)),
                ('taobao_user_nick', models.CharField(max_length=128)),
                ('sub_taobao_user_nick', models.CharField(max_length=64, null=True)),
                ('sub_taobao_user_id', models.CharField(max_length=32, null=True)),
                ('created_time', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_time', models.DateTimeField(auto_now=True, db_index=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
