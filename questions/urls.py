from django.conf.urls import url

from questions.views import questions_list, questions_detail

urlpatterns = [
    url(r'^$', questions_list, name='questions_list'),
    url(r'^best/$', questions_best, name="questions_best"),
    url(r'^tag/(?P<tag_name>[0-9]w+)/$', questions_with_tag, name="questions_with_tag"),
    url(r'^question/(?P<question_id>[0-9]+)/$', question_detail, name='question_detail'),
    url(r'^login/$', questions_login, name="questions_login"),
    url(r'^signup/$', questions_signup, name="questions_signup"),
    url(r'^ask/$', questions_ask, name="questions_ask")
]
