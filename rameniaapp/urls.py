from django.urls import path, include
from django.contrib.auth.views import LoginView
from rameniaapp.forms import PrettyAuthenticationForm

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # Noodle view and noodle actions
    path('noodle/<int:noodle_id>', views.view_noodle, name="noodle"),
    path('noodle/add', views.ramen_create_view, name="add_noodle"),
    path('noodle/<int:noodle_id>/edit', views.ramen_edit_view, name="edit_ramen"),
    path('noodle/<int:noodle_id>/review', views.ramen_review_view, name="review_ramen"),
    path('noodle/<int:id>/report', views.NoodleReportForm.as_view(), name="noodle_report"), 
    
    # User related views and report page
    path('user/<int:user_id>', views.view_profile, name="profile"),
    path('user/<int:user_id>/follow', views.follow_profile, name ="follow_profile"),
    path('user/<int:user_id>/following', views.view_following, name ="following"),
    path('user/<int:id>/report', views.ProfileReportForm.as_view(), name="profile_report"), 
    
    # Routes for the default django authentication module and our account action pages
    path('', include('django.contrib.auth.urls')),
    path('login', LoginView.as_view(template_name='registration/login.html', authentication_form=PrettyAuthenticationForm), name="login"),
    path('register', views.register, name="register"),
    path('edit_profile', views.edit_profile, name="edit_profile"),
    path('settings', views.change_password, name="change_password"),

    # Lists views
    path('list/<int:list_id>', views.view_list, name="list"),
    path('user/<int:user_id>/lists', views.view_user_lists, name="user_lists"),
    
    # Moderator links page
    path('mod', views.view_mod_page, name="moderator"),

    # Moderator edit views (including filtering- not yet fully implemented in UI) and actions
    path('mod/edits', views.EditsList.as_view(), name="all_edits"),
    path('mod/edits/noodle/new', views.EditsList.as_view(), {'new' : True}, name="new_noodles"),
    path('mod/edits/noodle/<int:noodle_id>', views.EditsList.as_view(), name="edits_by_noodle"),
    path('mod/edits/user/<int:user_id>', views.EditsList.as_view(), name="edits_by_user"),
    path('mod/edits/approve/<int:edit_id>', views.apply_edit, name="approve_edit"),
    path('mod/edits/reject/<int:edit_id>', views.reject_edit, name="reject_edit"),
    
    # Mod report views- filtering by object not yet implemented
    path('mod/reports/noodle/', views.NoodleReportList.as_view(), name="noodle_reports"),
    path('mod/reports/noodle/<int:item_id>', views.NoodleReportList.as_view(), name="reports_by_noodle"),
    path('mod/reports/review/', views.ReviewReportList.as_view(), name="review_reports"),
    path('mod/reports/review/<int:item_id>', views.ReviewReportList.as_view(), name="reports_by_review"),
    path('mod/reports/profile/', views.ProfileReportList.as_view(), name="profile_reports"),
    path('mod/reports/profile/<int:item_id>', views.ProfileReportList.as_view(), name="reports_by_profile"),

    # Mod report actions
    path('mod/reports/<int:report_id>/ignore', views.ignore_report, name="ignore_report"),
    path('mod/reports/<int:report_id>/status/<str:status>', views.update_report_status, name="update_report_status"),
    path('mod/reports/<str:report_type>/ban/<int:user_id>', views.ban_user, name="ban_user"),
    path('mod/reports/<int:report_id>/edit/', views.ignore_report, name="report_edit"),
    path('mod/reports/<int:report_id>/delete_content/', views.delete_content, name="delete_content"),

    path('search', views.view_search, name="search"),
    path('notifications', views.view_notifications, name="notifications"),

    # REST API views

    # get the noodles of list_id
    path('api/list/<int:list_id>', views.list_rest, name="list_rest"),
    
    # modify list_id. PUT adds noodle_id to the list, DELETE removes noodle_id from the list
    path('api/list/<int:list_id>/<int:noodle_id>', views.list_mod_rest, name="list_mod_rest"),

    # returns a json list of user_id's lists
    path('api/user/<int:user_id>/lists', views.user_lists_rest, name="user_lists_rest"),

    # returns search results
    path('api/search', views.search_rest, name="search_rest"),

    # returns notification results
    path('api/notifications/<int:page>', views.notifications_rest, name="notifications_rest"),

    # returns a review
    path('api/review/<int:review>', views.review_rest, name="review_rest"),

    # returns reviews for a noodle
    path('api/reviews/<int:noodle>', views.reviews_rest, name="reviews_rest")
]


