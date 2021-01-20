from django.shortcuts import render
from django.http.response import HttpResponse
import random


def lottos(req):
    lotto = []
    for i in range (6):
        lotto.append(random.randint(1,46))
        lotto = list(set(lotto))
    return HttpResponse(f"lotto번호 추천 : {lotto}")
# Create your views here.
