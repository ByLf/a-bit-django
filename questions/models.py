# -*- coding: utf-8 -*-
from __future__ import unicode_literals

ffrom django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    upload = models.ImageField(upload_to='uploads/%Y/%m/%d/')
