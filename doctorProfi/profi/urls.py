from django.urls import path, re_path, register_converter
from profi import views
from . import converters

register_converter(converters.FourDigitYearConverter, "year4")

urlpatterns = [
    path('', views.index, name='home'),
    path('prices/', views.price, name='prices'),
    path('appointment/', views.create_appointment, name='create_appointment'),
    path('schedule/', views.schedule, name='schedule'),
    path('blog/', views.blog, name='blog'),

]
