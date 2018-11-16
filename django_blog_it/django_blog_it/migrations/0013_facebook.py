# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-22 09:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('django_blog_it', '0012_auto_20160722_0657'),
    ]

    operations = [
        migrations.CreateModel(
            name='Facebook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook_id', models.CharField(max_length=100)),
                ('facebook_url', models.CharField(default='', max_length=200)),
                ('first_name', models.CharField(default='', max_length=200)),
                ('last_name', models.CharField(default='', max_length=200)),
                ('verified', models.CharField(default='', max_length=200)),
                ('name', models.CharField(default='', max_length=200)),
                ('language', models.CharField(default='', max_length=200)),
                ('hometown', models.CharField(default='', max_length=200)),
                ('email', models.CharField(db_index=True, default='', max_length=200)),
                ('gender', models.CharField(default='', max_length=200)),
                ('dob', models.DateField(blank=True, null=True)),
                ('location', models.CharField(default='', max_length=200)),
                ('timezone', models.CharField(default='', max_length=200)),
                ('accesstoken', models.CharField(default='', max_length=2000)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='facebook', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]