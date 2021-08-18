from django.contrib.admin import ModelAdmin, register

from .models import Worker, Department, Director, OrderedWorker, EducationOffice, GeneralOffice


@register(Worker)
class WorkerAdmin(ModelAdmin):
    pass


@register(Department)
class DepartmentAdmin(ModelAdmin):
    pass


@register(Director)
class DirectorAdmin(ModelAdmin):
    pass


@register(OrderedWorker)
class OrderWorkerAdmin(ModelAdmin):
    pass


@register(EducationOffice)
class EducationOffice(ModelAdmin):
    pass


@register(GeneralOffice)
class GeneralOffice(ModelAdmin):
    pass
