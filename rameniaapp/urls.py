from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('noodle/<int:noodle_id>', views.view_noodle, name="noodle"),
    path('user/<int:user_id>', views.view_profile, name="profile"),
    path('user/<int:user_id>/follow', views.follow_profile, name ="follow_profile"),
    path('', include('django.contrib.auth.urls')),
    path('register', views.register, name="register"),
    path('edit_profile', views.edit_profile, name="edit_profile"),
    path('list/<int:list_id>', views.view_list, name="list"),
    path('user/<int:user_id>/lists', views.view_user_lists, name="user_lists"),
    path('search', views.view_search, name="search"),

    # REST API views

    # get the noodles of list_id
    path('api/list/<int:list_id>', views.list_rest, name="list_rest"),
    
    # modify list_id. PUT adds noodle_id to the list, DELETE removes noodle_id from the list
    path('api/list/<int:list_id>/<int:noodle_id>', views.list_mod_rest, name="list_mod_rest"),

    # returns a json list of user_id's lists
    path('api/user/<int:user_id>/lists', views.user_lists_rest, name="user_lists_rest"),

    # returns search results
    path('api/search', views.search_rest, name="search_rest"),
]
