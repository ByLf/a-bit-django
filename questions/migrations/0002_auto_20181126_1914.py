# Generated by Django 2.1.2 on 2018-11-26 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='likes',
            field=models.IntegerField(default=0, verbose_name='Лайки'),
        ),
        migrations.AddField(
            model_name='article',
            name='picture',
            field=models.ImageField(null=True, upload_to='uploads/%Y/%m/%d/'),
        ),
    ]
