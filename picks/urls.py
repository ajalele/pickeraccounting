from django.urls import path
from picks import views

app_name = 'picks'

urlpatterns = [
    path('', views.index, name='index'),
]