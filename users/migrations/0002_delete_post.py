# Generated by Django 2.2 on 2019-08-23 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Post',
        ),
    ]