# Generated by Django 3.1.5 on 2021-02-28 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movieapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usertype', models.IntegerField(choices=[(1, '普通用户'), (2, 'VIP'), (3, 'SVIP')])),
                ('username', models.CharField(max_length=32)),
                ('userpassword', models.CharField(max_length=32)),
            ],
            options={
                'db_table': 'User',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='UserToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=64)),
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='movieapi.user')),
            ],
            options={
                'db_table': 'UserToken',
                'managed': True,
            },
        ),
    ]
