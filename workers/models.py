from django.db import models
from django.db.models import Manager


class WorkerManager(models.Manager):
    """
    Менеджер для работы с активными сотрудниками
    """
    def get_queryset(self):
        """
        Переопределенный кверисет с фильтрацией сотрудников с заданной датой принятия на работу и с не пустым табельным номером отличным от 0
        """

        return super(WorkerManager, self).get_queryset().filter(startwork_date__isnull=False).exclude(tab_num=0)

    def get_workers_info(self):
        """
            Получение  списка строк в которых содержится
        фамилия, имя, табельный номер сотрудника а также название подразделения в котором числится
        Строки упорядочены по фамилии и имени сотрудника.
        Каждая строка должна быть в формате вида: Васильев Василий, 888, Подразделение №1
        """

        queryset = super(WorkerManager, self).get_queryset().values(
            'first_name',
            'last_name',
            'tab_num',
            'department__name',
        ).order_by('first_name', 'last_name',)
        list_workers = []
        for worker in queryset:
            list_workers.append(
                f'{worker.get("first_name")} {worker.get("last_name")}, '
                f'{worker.get("tab_num")}, {worker.get("department__name")}'
            )
        return list_workers


class Department(models.Model):
    name = models.CharField('Наименование', max_length=30)

    @property
    def get_active_worker_count(self):
        """
        Количество активных сотрудников подразделения
        """
        return Worker.objects.filter(department=self).count()

    @property
    def get_all_worker_count(self):
        """
        Количество всех сотрудников подразделения
        """
        return Worker.objects_all.filter(department=self).count()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'department'
        verbose_name = 'Департамент'
        verbose_name_plural = 'Департаменты'


class Worker(models.Model):
    """
    Сотрудник
    """

    objects = WorkerManager()
    objects_all = Manager()

    first_name = models.CharField('Имя', max_length=30)
    last_name = models.CharField('Фамилия', max_length=30)
    startwork_date = models.DateField('Дата выхода на работу', null=True, )
    tab_num = models.IntegerField('Табельный номер', default=0)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.last_name} {self.first_name}'

    class Meta:
        db_table = 'workers'
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
