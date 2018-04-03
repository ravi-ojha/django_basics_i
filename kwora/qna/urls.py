from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.question_list, name='question_list'),
    url(r'^question/(?P<question_id>\d+)/$', views.question_detail, name='question_detail'),
]
