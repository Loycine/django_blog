# Generated by Django 3.0.7 on 2020-08-06 09:25

from django.db import migrations
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200806_0855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=mdeditor.fields.MDTextField(verbose_name='正文'),
        ),
    ]
