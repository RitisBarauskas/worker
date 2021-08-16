from django.shortcuts import render
from django.http import HttpResponse
from .models import Department, Worker


def index(request):
    res = Worker.objects.get_workers_info()
    print(res)
    return HttpResponse(res)
