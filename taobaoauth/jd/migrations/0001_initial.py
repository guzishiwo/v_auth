# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JdToken',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('access_token', models.CharField(max_length=128)),
                ('code', models.IntegerField()),
                ('expires_in', models.IntegerField()),
                ('refresh_token', models.CharField(max_length=128)),
                ('scope', models.CharField(max_length=16, null=True)),
                ('time', models.CharField(max_length=32)),
                ('token_type', models.CharField(max_length=16)),
                ('uid', models.CharField(max_length=128)),
                ('user_nick', models.CharField(max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
