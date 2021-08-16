from django.contrib.admin import ModelAdmin, register
from .models import Department, Worker


@register(Worker)
class WorkerAdmin(ModelAdmin):
    pass


@register(Department)
class DepartmentAdmin(ModelAdmin):
    pass
