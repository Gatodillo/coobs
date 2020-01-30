# Generated by Django 2.2.2 on 2020-01-30 18:27

import datetime
from decimal import Decimal
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
            ],
            options={
                'verbose_name': 'partner',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Cooperative',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=128, verbose_name='name')),
                ('business_name', models.CharField(max_length=128, unique=True, verbose_name='business name')),
                ('starting_date', models.DateField(default=datetime.date.today, verbose_name='starting date')),
                ('is_active', models.BooleanField(default=False, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
            ],
            options={
                'verbose_name': 'cooperative',
            },
        ),
        migrations.CreateModel(
            name='MainPrinciple',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='name')),
                ('name_key', models.CharField(max_length=256)),
                ('description', models.CharField(default='', max_length=1024)),
                ('description_es', models.CharField(default='', max_length=1024, null=True)),
                ('description_en', models.CharField(default='', max_length=1024, null=True)),
                ('description_key', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Principle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='description')),
                ('visible', models.BooleanField(default=True)),
                ('cooperative', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Cooperative', verbose_name='cooperative')),
                ('main_principle', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.MainPrinciple', verbose_name='main principle')),
            ],
            options={
                'verbose_name': 'principle',
            },
        ),
        migrations.CreateModel(
            name='Period',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=256, null=True, verbose_name='name')),
                ('date_from', models.DateField(default=datetime.date.today, verbose_name='date from')),
                ('date_to', models.DateField(default=datetime.date.today, verbose_name='date to')),
                ('actions_budget', models.DecimalField(decimal_places=2, max_digits=19, verbose_name='actions budget')),
                ('cooperative', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Cooperative', verbose_name='cooperative')),
            ],
            options={
                'verbose_name': 'period',
            },
        ),
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today, verbose_name='date')),
                ('name', models.CharField(max_length=256, verbose_name='name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('invested_money', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0.00'), max_digits=19, verbose_name='invested money')),
                ('public', models.BooleanField(default=True)),
                ('cooperative', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Cooperative', verbose_name='cooperative')),
                ('partners_involved', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='partners involved')),
                ('principles', models.ManyToManyField(to='api.Principle', verbose_name='principles')),
            ],
            options={
                'verbose_name': 'action',
            },
        ),
        migrations.AddField(
            model_name='partner',
            name='cooperative',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Cooperative', verbose_name='cooperative'),
        ),
        migrations.AddField(
            model_name='partner',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='partner',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
