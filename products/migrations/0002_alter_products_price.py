# Generated by Django 3.2 on 2021-05-04 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.IntegerField(verbose_name='قمیت'),
        ),
    ]
