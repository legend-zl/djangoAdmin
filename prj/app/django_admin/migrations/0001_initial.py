# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-24 12:41
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_admin.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
    ]

    operations = [
        migrations.CreateModel(
            name='profileUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=30, unique=True, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.')], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('userType', models.CharField(choices=[('gl', '\u7ba1\u7406\u5458'), ('md', '\u666e\u901a\u7528\u6237')], default='md', max_length=2, verbose_name='\u7528\u6237\u7c7b\u578b')),
                ('userna', models.CharField(default='first', max_length=100, unique=True, verbose_name='\u4f5c\u4e3a\u4e3b\u952e\u7684\u5b57\u6bb5')),
                ('UserIsSuper', models.BooleanField(default=False, verbose_name='\u662f\u5426\u662f\u8d85\u7ea7\u7528\u6237')),
            ],
            options={
                'db_table': 'auth_user',
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', django_admin.models.CustomUserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyCode', models.CharField(max_length=80, unique=True, verbose_name='\u5ba2\u6237\u4ee3\u7801')),
                ('companyName', models.CharField(max_length=80, unique=True, verbose_name='\u5ba2\u6237\u540d\u79f0')),
                ('isvalue', models.BooleanField(default=True, verbose_name='\u5f53\u524d\u662f\u5426\u6709\u6548')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='\u90ae\u7bb1')),
                ('contactor', models.CharField(blank=True, max_length=30, null=True, verbose_name='\u8054\u7cfb\u4eba')),
                ('phone', models.CharField(blank=True, max_length=30, null=True, verbose_name='\u8054\u7cfb\u7535\u8bdd')),
                ('datestart', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='\u670d\u52a1\u5f00\u59cb\u65f6\u95f4')),
                ('datefinish', models.DateTimeField(blank=True, null=True, verbose_name='\u670d\u52a1\u7ed3\u675f\u65f6\u95f4')),
            ],
            options={
                'db_table': 'auth_company',
                'verbose_name': '\u5ba2\u6237',
                'verbose_name_plural': '\u5ba2\u6237',
            },
            managers=[
                ('objects', django_admin.models.CompanyManager()),
            ],
        ),
        migrations.CreateModel(
            name='Departclass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.DecimalField(decimal_places=1, max_digits=10, unique=True, verbose_name='\u7ea7\u522b')),
                ('name', models.CharField(max_length=80, unique=True, verbose_name='\u7ea7\u522b\u540d\u79f0')),
            ],
            options={
                'db_table': 'auth_departclass',
                'verbose_name': '\u7ea7\u522b',
                'verbose_name_plural': '\u7ea7\u522b',
            },
            managers=[
                ('objects', django_admin.models.DepartclassManager()),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departCode', models.CharField(max_length=80, verbose_name='\u5355\u4f4d\u4ee3\u7801')),
                ('departName', models.CharField(max_length=80, verbose_name='\u5355\u4f4d\u540d\u79f0')),
                ('lng', models.DecimalField(blank=True, decimal_places=8, max_digits=15, null=True, verbose_name='\u7ecf\u5ea6')),
                ('lat', models.DecimalField(blank=True, decimal_places=8, max_digits=15, null=True, verbose_name='\u7eac\u5ea6')),
                ('address', models.CharField(blank=True, max_length=100, null=True, verbose_name='\u5355\u4f4d\u5730\u5740')),
                ('email', models.EmailField(max_length=254, verbose_name='\u90ae\u7bb1')),
                ('contactor', models.CharField(blank=True, max_length=30, null=True, verbose_name='\u8054\u7cfb\u4eba')),
                ('phone', models.CharField(blank=True, max_length=30, null=True, verbose_name='\u8054\u7cfb\u7535\u8bdd')),
                ('datejoined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('company', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='django_admin.Company', verbose_name='\u5ba2\u6237\u540d\u79f0')),
                ('departFather', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='django_admin.Department', verbose_name='\u4e0a\u7ea7\u5355\u4f4d')),
                ('departclass', models.ForeignKey(default=10, on_delete=django.db.models.deletion.CASCADE, to='django_admin.Departclass', verbose_name='\u5355\u4f4d\u7ea7\u522b')),
            ],
            options={
                'db_table': 'auth_department',
                'verbose_name': '\u5355\u4f4d',
                'verbose_name_plural': '\u5355\u4f4d',
            },
            managers=[
                ('objects', django_admin.models.DepartmentManager()),
            ],
        ),
        migrations.AddField(
            model_name='profileuser',
            name='department',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='django_admin.Department', verbose_name='\u5355\u4f4d\u540d\u79f0'),
        ),
        migrations.AddField(
            model_name='profileuser',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='profileuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.AlterUniqueTogether(
            name='department',
            unique_together=set([('departCode', 'company')]),
        ),
        migrations.AlterUniqueTogether(
            name='profileuser',
            unique_together=set([('username', 'department')]),
        ),
    ]
