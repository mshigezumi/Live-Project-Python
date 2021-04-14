from django.urls import path
from . import views

urlpatterns = [
    path('', views.tanksHome, name='tanksHome'),
    path('gallery/', views.tanksGallery, name='tanksGallery'),
    path('videos/', views.tanksVideos, name='tanksVideos'),
    path('contact/', views.tanksContact, name='tanksContact'),
    path('admin/', views.tanksAdmin, name='tanksAdmin'),
    path('<int:pk>/details/', views.tanksDetails, name='tanksDetails'),
    path('<int:pk>/edit/', views.tanksEdit, name='tanksEdit'),
    path('<int:pk>/delete/', views.tanksDelete, name='tanksDelete'),
    path('confirm/', views.tanksConfirm, name='tanksConfirm'),
    path('create/', views.tanksCreate, name='tanksCreate'),
    path('list/', views.tanksList, name='tanksList'),
    path('API/', views.tanksAPI, name='tanksAPI'),
    path('soup/', views.tanksSoup, name='tanksSoup'),
]