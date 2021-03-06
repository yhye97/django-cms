# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-04 08:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='카테고리 이름')),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('is_blocked', models.BooleanField(default=False, verbose_name='노출 제한')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='작성일')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.Member', verbose_name='작성자')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='제목')),
                ('subtitle', models.CharField(max_length=255, verbose_name='부제목')),
                ('content', models.TextField(verbose_name='내용')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='삭제된 글')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='작성일')),
                ('deleted_at', models.DateTimeField(auto_now_add=True, verbose_name='삭제일')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.Category', verbose_name='카테고리')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.Member', verbose_name='작성자')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.Post', verbose_name='원본글'),
        ),
    ]
