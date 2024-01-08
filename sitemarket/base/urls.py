from django.urls import path, register_converter
from base import views
from . import converters

register_converter(converters.FourDigitYearConverter, "year4")

urlpatterns = [
    path('', views.index),
    path('goods/<int:good_id>/', views.goods),
    path('goods/<slug:good_slug>/', views.goods_by_slug),
    path('archive/<year4:year>/', views.archive)
    ]

