# Generated by Django 3.2 on 2021-05-04 16:31

from django.db import migrations, models
import setting_site.models


class Migration(migrations.Migration):

    dependencies = [
        ('setting_site', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='نام و نام خانوادگی')),
                ('image', models.ImageField(blank=True, null=True, upload_to=setting_site.models.upload_image_path, verbose_name='تصویر')),
                ('body', models.TextField(max_length=350, verbose_name='درباره خود')),
            ],
            options={
                'verbose_name_plural': 'کارمندان',
            },
        ),
    ]
