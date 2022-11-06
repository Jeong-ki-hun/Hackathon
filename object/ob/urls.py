from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('seoul/', views.index, name='index'),
    path('', views.shop_list, name='shop_list'),
    # ex: /polls/5/
    ]