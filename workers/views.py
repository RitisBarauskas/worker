from django.shortcuts import render
from django.http import HttpResponse
from .models import Department, Worker


def index(request):
    HttpResponse('Это тестовая страница')
