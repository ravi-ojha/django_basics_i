# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Question

# Create your views here.
def question_list(request):
    questions = Question.objects.all()
    return render(request, 'qna/question_list.html', context={'questions': questions})


def question_detail(request, question_id):
    question = Question.objects.get(id=question_id)
    answers = question.answer_set.all()
    context_data = {
        'question': question,
        'answers': answers,
    }
    return render(request, 'qna/question_detail.html', context=context_data)
