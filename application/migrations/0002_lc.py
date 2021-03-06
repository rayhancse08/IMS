# Generated by Django 2.2 on 2019-09-22 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lc_no', models.CharField(max_length=100, unique=True)),
                ('issue_bank', models.CharField(max_length=100)),
                ('issue_date', models.DateField()),
                ('expire_date', models.DateField()),
                ('client_name', models.CharField(max_length=100)),
                ('client_bank_name', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]
