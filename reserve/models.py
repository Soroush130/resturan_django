from django.db import models


# Create your models here.

class Reseve(models.Model):
    name = models.CharField(verbose_name='نام و نام خانوادگی', max_length=300)
    number = models.CharField(verbose_name='تعداد افراد', max_length=300)
    phone = models.CharField(verbose_name='شماره تلفن', max_length=300)
    time = models.TimeField(verbose_name='زمان', max_length=300)
    date = models.DateField(verbose_name='تاریخ', max_length=300)
    occasion = models.CharField(verbose_name='مناسبت', max_length=300)

    class Meta:
        verbose_name = 'رزرو'
        verbose_name_plural = 'رزورها'

    def __str__(self):
        return self.name