from django.shortcuts import render
from django.http import HttpResponse
from .models import Department, Worker


def index(request):
    # departments = Department.get_all_worker_count()
    # return HttpResponse(departments)

    workers = Worker.objects.get_workers_info()
    return HttpResponse(workers)
