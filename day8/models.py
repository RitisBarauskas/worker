from django.db import models


class WorkerManager(models.Manager):
    """
    Менеджер для работы с активными сотрудниками
    """
    def get_queryset(self):
        """
        Переопределенный кверисет возвращающий всех сотрудников без директоров
        """

        return super(WorkerManager, self).get_queryset().exclude(director__isnull=False)


class Office(models.Model):
    """
    Офисы компании
    """
    address = models.TextField('Адрес')
    mail = models.CharField('Адрес почты', max_length=30, )

    class Meta:
        abstract = True


class EducationOffice(Office):
    """
    Учебный офис
    """
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.address

    class Meta:
        db_table = 'education_office'
        verbose_name = 'Учебный офис'
        verbose_name_plural = 'Учебные офисы'


class GeneralOffice(Office):
    """
    Головной офис
    """
    name = models.TextField('Название головного офиса ')

    def __str__(self):
        return self.address

    class Meta:
        db_table = 'office'
        verbose_name = 'Головной офис'
        verbose_name_plural = 'Головные офисы'


class Department(models.Model):
    """
    Подразделение
    """
    name = models.CharField('Наименование', max_length=30)
    education_office = models.ForeignKey(EducationOffice, on_delete=models.SET_NULL, null=True )
    office = models.ForeignKey(GeneralOffice, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'department'
        verbose_name = 'Департамент'
        verbose_name_plural = 'Департаменты'


class Person(models.Model):
    """
    Физическое лицо
    """
    first_name = models.CharField('Фамилия', max_length=30)
    last_name = models.CharField('Имя', max_length=30)

    class Meta:
        abstract = True


class Worker(Person):
    """
    Сотрудник
    """
    objects = WorkerManager()
    objects_all = models.Manager()
    startwork_date = models.DateField('Дата выхода на работу', null=True, )
    tab_num = models.IntegerField('Табельный номер', default=0)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def get_status(self):
        return f'{self.first_name} работает с {self.startwork_date}'

    class Meta:
        db_table = 'workers'
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class OrderedWorker(Worker):
    """
    Модель с  сотрудниками упорядоченными по фамилии и дате приема на работу
    """
    @property
    def startwork_year(self):
        """
        Получить значение года приема на работу
        """
        return self.startwork_date.year

    def __str__(self):
        return f'Принят на работу: {self.startwork_date} || {self.last_name} {self.first_name}'

    class Meta:
        ordering=('first_name', 'startwork_date')
        proxy=True


class Director(Worker):
    """
    Директор
    """
    objects = models.Manager()
    grade = models.IntegerField('Оценка', default=1)

    class Meta:
        db_table = 'directors'
        verbose_name = 'Директор'
        verbose_name_plural = 'Директора'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
