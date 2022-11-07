from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('map/',views.map, name='map'),
    path('seoul/', views.index, name='index'),
    path('', views.shop_list, name='shop_list'),
    # ex: /polls/5/
    ]