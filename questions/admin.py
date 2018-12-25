# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from question.models import Author, Article

# Register your models here.

admin.site.register(Author)
admin.site.register(Article)
