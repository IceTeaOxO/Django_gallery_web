from django.urls import path
from . import views
urlpatterns = [
    path('', views.add),
    path('index/', views.add),
    path('gallery/', views.detail),
    
]