from django.db import models


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
# QUANTITY MODELS
#######################


class QuantitySchool(models.Model):
    """ Модель Формы обучения """

    title = models.CharField('Форма обучения', max_length=599, blank=True)

    is_active = models.BooleanField('Активный', default=True)
    created_date = models.DateTimeField('Дата создания', auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Дата обновления", auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'форму'
        verbose_name_plural = 'Форма обучения'


class DBLicense(models.Model):
    """ Модель Базы лицензии """

    STATUS_CHOICES = [
        ('issued', 'Выдан'),
        ('suspended', 'Приостановлен'),
        ('revoked', 'Аннулирован'),
    ]

    number_register = models.CharField('Номер регистрации', unique=True, max_length=599, blank=True)
    name_entity = models.CharField('Наименование юр лиц', max_length=599, blank=True)
    tax_name = models.CharField('Идентификационный номер', max_length=599, blank=True)
    entity_address = models.CharField('Юридический адрес', max_length=599, blank=True)
    address_program = models.CharField('Адрес реализационной прг', max_length=599, blank=True)
    cipher = models.CharField('Шифр', max_length=599, blank=True)
    title_school = models.CharField('Наименование оброзовательной учр', max_length=599, blank=True)
    quantity_school = models.CharField('Кол. обучающих', max_length=599, blank=True)
    issuing_license = models.CharField('Основание выдачи', max_length=599, blank=True)
    data_license = models.DateTimeField('Дата выдачи')
    form_number = models.CharField('Номер и серия бланка', max_length=599, blank=True)
    form_number_suspended = models.CharField('Основание срок приостанавления', max_length=599, blank=True)
    form_number_start = models.CharField('Основание дата возобновления', max_length=599, blank=True)
    form_number_stop = models.CharField('Основание дата прекращения', max_length=599, blank=True)
    data_address = models.CharField('Данные о смене адреса', max_length=599, blank=True)
    form_number_data = models.CharField('Основание дата выдачи дубликата', max_length=599, blank=True)

    file = models.FileField('Вставка файла', upload_to='file/', blank=True)
    status = models.CharField('Статус', max_length=20, choices=STATUS_CHOICES, default='issued')

    issuing_authorities = models.ForeignKey(IssuingAuthority, verbose_name='Орган выдачи', on_delete=models.CASCADE)
    regions = models.ForeignKey(Region, verbose_name='Регион', on_delete=models.CASCADE)
    quantities = models.ForeignKey(QuantitySchool, verbose_name='Форма обучения', on_delete=models.CASCADE)

    is_active = models.BooleanField('Активный', default=True)
    created_date = models.DateTimeField('Дата создания', auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Дата обновления", auto_now=True)

    def __str__(self):
        return self.number_register

    class Meta:
        verbose_name = 'лицензию'
        verbose_name_plural = 'База лицензии'
