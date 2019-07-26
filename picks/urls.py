from django.urls import path
from picks import views

app_name = 'picks'

urlpatterns = [
    path('', views.index, name='index'),
    path('enterpick/', views.enter_pick, name='enterpick'),
    path('register/', views.register, name='register'),
    path('soldlist/', views.sold_list, name='soldlist'),
    path('soldpick/<int:id>/', views.sold_pick, name='soldpick'),
]