# Generated by Django 3.2 on 2021-05-04 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_categoryproducts'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='categories',
            field=models.ManyToManyField(blank=True, to='products.CategoryProducts', verbose_name='دسته بندی ها'),
        ),
    ]
