# -*- coding: utf-8 -*-
from __future__ import unicode_literals

ffrom django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime

# Create your models here.
class User(AbstractUser):
    upload = models.ImageField(upload_to='uploads/%Y/%m/%d/')

class Tags(models.Model):
    tag = ManyToMany(Post)

class answers(models.Model):
    title = models.TextField(verbose_name=u"Комментарий")
    correct = BooleanField(default=True, verbose_name=u"корректность комментария")


class Question(models.Model):
    title = models.CharField(max_length=120, verbose_name=u"Заголовок вопроса")
    text = models.TextField(verbose_name=u"Полное описание вопроса")

    create_date = models.DateTimeField(default=datetime.now, verbose_name=u"Время создания вопроса")
    answers = OneToMany(answers)

    is_active = models.BooleanField(default=True, verbose_name=u"Доступность вопроса")
    likes = models.IntegerField(verbose_name='Лайки', default=0)
    picture = models.ImageField(upload_to='uploads/%Y/%m/%d/', null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    answers = models.ForeignKey(answers, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-create_date']
