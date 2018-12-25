# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from questions.models import Question

import json
import requests

from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from question.forms import AuthorForm, ArticleForm
from question import models

#my views
#по-хорошему, эти 2 должны быть как ленивая загрузка
def popTag(request):
    #list_tag = ["perl","django","TechnoPark","MySQL","Firefox","IE","python","php"]
    list_tag = Tags.objects.filter(8)#
    return render(request, 'popTag.html', {'list_tag': list_tag})

def bestMembers(request):
    #dist_bestMembers = [("Borka", "href"),("Mr.Smit", "href"),("Salem", "href"),("Cocil", "href"),("Koks", "href")]
    dist_Members = user.objects.filter(5)
    return render(request, 'bestMembers.html', {'dist_bestMembers': dist_bestMembers})

def header(request):
    this_user = user.objects.filter(user = nick)
    #ref_avatar = 'href'
    ref_avatar = this_user.avatar
    #nick = "Baam"
    nick = this_user.name
    return render(request, 'header.html', {'ref_avatar': ref_avatar, 'nick': nick})

def index(request):
    questions_list = [
        {"name": "my best questiion", "id": 1},
        {"name": "my best questiion2", "id": 2},
    ]
    return render(request, "question/index.html", {
        "questions": questions_list,
    })
def add_author(request):
    form = AuthorForm()
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('authors')
    return render(request, "question/add_form.html", {"form": form})


def questions_list(request):
    contact_list = Question.objects.filter(is_active=True)
    paginator = Paginator(contact_list, 2)
    page = request.GET.get('page')
    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)

    return render(request, 'questions_list.html', {'questions': questions, 'title':"Recent questions"})

def questions_best(request):
    contact_list = Question.objects.filter(is_active=True)#add sort
    paginator = Paginator(contact_list, 2)

    page = request.GET.get('page')
    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)

    return render(request, 'questions_list.html', {'questions': questions, 'title':"Best questions"})

def questions_detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    return render(request, 'questions_detail.html', {'title': question.title, 'textMessage': question.text, 'answers': question.answers})

def questions_with_tag(request, question_tag):
    contact_list = Question.objects.filter(is_active=True & tag=question_tag)
    paginator = Paginator(contact_list, 2)  # По 2 на страницу

    page = request.GET.get('page')
    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)

    return render(request, 'questions_list.html', {'questions': questions, 'title': "tag: "+question_tag})

require_POST
def like_article(request):
    article_id = request.POST.get('article_id', '')
    article = models.Article.objects.filter(id=article_id).first()
    if not article:
        return JsonResponse({"status": "error"})

    article.likes += 1
    article.save()

    return JsonResponse({"status": "ok"})


def send_message(article):
    command = {
        "method": "publish",
        "params": {
            "channel": "new_posts",
            "data": {
                "article": article.id,
                "article_text": article.text,
            }
        }
    }
    headers = {
        'Content-type': 'application/json',
        'Authorization': 'apikey ' + settings.CENTRIFUGO_KEY
    }
    requests.post(
        "http://{}/api".format(settings.CENTRIFUGO_HOST),
        data=json.dumps(command),
        headers=headers
    )
