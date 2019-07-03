from django.urls import path
from AppTwo import views


urlpatterns = [
    path('help/', views.index_template, name = 'index_template'),
]