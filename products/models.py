from django.db import models
import os
from django.utils import timezone


# Create your models here.

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f"products/{final_name}"


class CategoryProducts(models.Model):
    title = models.CharField(max_length=100, verbose_name='نام دسته بندی')

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return self.title


class ProductsManager(models.Manager):

    def get_products_by_category_1(self):
        return self.get_queryset().filter(categories__title__iexact='پیش غذا', active=True)

    def get_products_by_category_2(self):
        return self.get_queryset().filter(categories__title__iexact='غذاهای اصلی', active=True)

    def get_products_by_category_3(self):
        return self.get_queryset().filter(categories__title__iexact='دسر ها', active=True)

    def get_products_by_category_4(self):
        return self.get_queryset().filter(categories__title__iexact='نوشیدنی ها', active=True)

    def get_special_today(self):
        return self.get_queryset().filter(Special_today=True)


class Products(models.Model):
    title = models.CharField(max_length=50, verbose_name='نام غذا')
    price = models.IntegerField(verbose_name='قمیت')
    body = models.TextField(max_length=250, verbose_name='توضیح کوتاه در باره غذا')
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True, verbose_name='تصویر')

    categories = models.ManyToManyField(CategoryProducts, blank=True, verbose_name="دسته بندی ها")

    active = models.BooleanField(verbose_name='فعال / غیر فعال', default=True)
    Special_today = models.BooleanField(verbose_name='مخصوص امروز', default=False)
    # time_food = models.DateTimeField(default=timezone.now)

    objects = ProductsManager()

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    def __str__(self):
        return self.title


class Gallery(models.Model):
    text = models.TextField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='gallery-foods')
