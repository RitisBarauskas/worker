from django.shortcuts import render
from django.http import HttpResponse
from .models import Department, Worker


def index(request):
    workers = Worker.objects.all()
    return HttpResponse(workers)
