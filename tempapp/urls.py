from django.urls import path
from . import views

urlpatterns = [
    path('tempapp',views.index, name='index'),
    path('',views.temp_demo, name='index1')
]