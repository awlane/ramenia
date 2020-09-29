from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('noodle/<int:noodle_id>', views.view_noodle, name="noodle"),
    path('', include('django.contrib.auth.urls')),
]
