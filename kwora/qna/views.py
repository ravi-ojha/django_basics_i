# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Question

# Create your views here.
def question_list(request):
    questions = Question.objects.all()
    return render(request, 'qna/question_list.html', context={'questions': questions})
