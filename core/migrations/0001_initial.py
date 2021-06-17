# Generated by Django 3.2.4 on 2021-06-15 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payer', models.CharField(help_text='Payer name', max_length=255, verbose_name='payer')),
                ('points', models.IntegerField(help_text='Points', verbose_name='points')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='PointBalance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payer', models.CharField(help_text='Payer name', max_length=255, verbose_name='payer')),
                ('points', models.IntegerField(help_text='Points', verbose_name='points')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Spend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payer', models.CharField(help_text='Payer name', max_length=255, verbose_name='payer')),
                ('points', models.IntegerField(help_text='Points', verbose_name='points')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]