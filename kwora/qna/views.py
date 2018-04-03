# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


# Create your views here.
def question_list(request):
    return render(request, 'qna/question_list.html', context={})
