from django.urls import path

from . import views

urlpatterns = [
    path('api/place/<int:pk>/', views.detail_api, name='detail_api'),
    path('place/<int:pk>/', views.detail, name='detail'),
    path('', views.index, name='index'),
]
