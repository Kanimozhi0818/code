# Generated by Django 2.2.4 on 2022-06-25 07:08

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AA_Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('zip', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='CUA_Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('zip', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Register_Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('zip', models.CharField(max_length=50)),
                ('user_type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Upload_File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='File Name')),
                ('file', models.FileField(null=True, upload_to='', verbose_name='File')),
                ('notes', models.TextField(max_length=2000, verbose_name='Notes')),
                ('date', models.DateField(default=datetime.datetime(2022, 6, 25, 7, 8, 53, 589605, tzinfo=utc), verbose_name='Uploaded Date')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Register_Detail')),
            ],
        ),
        migrations.CreateModel(
            name='File_Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public_key', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Public Key')),
                ('private_key', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Private Key')),
                ('cua_public_key', models.CharField(blank=True, max_length=1000, null=True, verbose_name='CUA Public Key')),
                ('cua_private_key', models.CharField(blank=True, max_length=1000, null=True, verbose_name='CUA Private Key')),
                ('status', models.CharField(max_length=1000, verbose_name='Status')),
                ('file_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Upload_File')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Register_Detail')),
            ],
        ),
    ]
