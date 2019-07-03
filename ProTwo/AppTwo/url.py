from django.urls import path
from AppTwo import views


urlpatterns = [
    path('help/', views.index_template, name = 'index_template'),
    path('django_img/', views.static_files, name = 'static_django_guitar_img'),
]