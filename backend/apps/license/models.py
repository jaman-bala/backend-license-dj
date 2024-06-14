from django.db import models
from django.contrib.auth.models import User

#######################
# REGION MODELS
#######################

class Region(models.Model):
    """ Модель Региона """

    title = models.CharField('Наименование региона', max_length=599, blank=True)
    is_active = models.BooleanField('Активный', default=True)
    created_date = models.DateTimeField('Дата создания', auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Дата обновления", auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'регион'
        verbose_name_plural = 'Регионы'


#######################
# ISSUING MODELS
#######################

class IssuingAuthority(models.Model):
    """ Модель органа выдачи """

    title = models.CharField('Орган выдачи', max_length=599, blank=True)
    is_active = models.BooleanField('Активный', default=True)
    created_date = models.DateTimeField('Дата создания', auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Дата обновления", auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'орган'
        verbose_name_plural = 'Орган выдачи'



#######################
# STATUS MODELS
#######################

class CodeLicense(models.Model):
    """ Модель STATUS """

    title = models.CharField('Статус', max_length=199, blank=True)
    is_active = models.BooleanField('Активный', default=True)
    created_date = models.DateTimeField('Дата создания', auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Дата обновления", auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


#######################
# DB-LICENSE MODELS
#######################

class DBLicense(models.Model):
    """ Модель Базы лицензий """

    number_register = models.CharField('Номер регистрации', unique=True, max_length=999, blank=True)
    name_entity = models.CharField('Наименование юр. лица', max_length=599, blank=True)
    tax_name = models.CharField('Идентификационный номер', max_length=599, blank=True)
    entity_address = models.CharField('Юридический адрес', max_length=599, blank=True)
    address_program = models.CharField('Адрес реализационной программы', max_length=599, blank=True)
    cipher = models.CharField('Шифр', max_length=599, blank=True)
    issuing_license = models.CharField('Основание выдачи', max_length=1099, blank=True)
    data_license = models.DateTimeField('Дата выдачи')
    form_number = models.CharField('Номер и серия бланка', max_length=599, blank=True)
    form_number_suspended = models.CharField('Основание срок приостановления', max_length=2099, blank=True)
    form_number_start = models.CharField('Основание дата возобновления', max_length=2099, blank=True)
    form_number_stop = models.CharField('Основание дата прекращения', max_length=2099, blank=True)
    data_address = models.CharField('Данные о смене адреса', max_length=1099, blank=True)
    form_number_data = models.CharField('Основание дата выдачи дубликата', max_length=599, blank=True)
    term = models.CharField('Срок действия', max_length=599, blank=True)

    title_school = models.JSONField('Наименование образовательного учреждения', max_length=599, blank=True)
    quantity_school = models.JSONField('Кол. обучающихся', max_length=599, blank=True)
    quantities = models.JSONField('Форма обучения', max_length=599, blank=True)

    file = models.FileField('Вставка файла', upload_to='file/', blank=True)

    code_status = models.ForeignKey(CodeLicense, verbose_name='Статус выдачи', on_delete=models.CASCADE)
    issuing_authorities = models.ForeignKey(IssuingAuthority, verbose_name='Орган выдачи', on_delete=models.CASCADE)
    regions = models.ForeignKey(Region, verbose_name='Регион', on_delete=models.CASCADE)

    # user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    is_active = models.BooleanField('Активный', default=True)
    created_date = models.DateTimeField('Дата создания', auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Дата обновления", auto_now=True)

    def __str__(self):
        return self.number_register

    class Meta:
        verbose_name = 'База лицензие'
        verbose_name_plural = 'База лицензии'
