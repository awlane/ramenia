from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('noodle/<int:noodle_id>', views.view_noodle, name="noodle"),
    path('profile/<int:profile_id>', views.view_profile, name="profile"),
    path('', include('django.contrib.auth.urls')),
    path('register', views.register, name="register"),
    path('list/<int:list_id>', views.view_list, name="list"),

    path('api/list/<int:list_id>', views.list_rest, name="list_rest"),
    path('api/list/<int:list_id>/<int:noodle_id>', views.list_mod_rest, name="list_mod_rest"),
    path('api/user/<int:user_id>/lists', views.user_lists_rest, name="user_lists_rest"),
]
