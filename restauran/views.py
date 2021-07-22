from django.shortcuts import render
from products.models import Products, Gallery
from setting_site.models import AboutUs, SiteSetting, TeamUs


def home_page(request):
    categories_1 = Products.objects.get_products_by_category_1()
    categories_2 = Products.objects.get_products_by_category_2()
    categories_3 = Products.objects.get_products_by_category_3()
    categories_4 = Products.objects.get_products_by_category_4()

    teams = TeamUs.objects.all()[:3]
    about_us = AboutUs.objects.first()
    site_setting = SiteSetting.objects.first()
    special_today = Products.objects.get_special_today()
    gallery_food = Gallery.objects.all()
    context = {
        'about': about_us,
        'site_setting': site_setting,
        'teams': teams,
        'special_today': special_today,
        'gallery_food': gallery_food,
        'categories_1': categories_1,
        'categories_2': categories_2,
        'categories_3': categories_3,
        'categories_4': categories_4,
    }
    return render(request, 'home_page.html', context)
