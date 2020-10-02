from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('noodle/<int:noodle_id>', views.view_noodle, name="noodle"),
    path('profile/<int:profile_id>', views.view_profile, name="profile"),
    path('', include('django.contrib.auth.urls')),
]
