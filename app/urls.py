from django.urls import path
from . import views
urlpatterns = [
path('home/',views.home,name="home"),
path('register/',views.register,name="register"),
path('', views.user_login, name='user_login'),
path('user_dashboard/', views.user_dashboard, name='user_dashboard'),
path('logout/', views.logout, name='logout'),
path('aa_login/', views.aa_login, name='aa_login'),
path('aa_dashboard/', views.aa_dashboard, name='aa_dashboard'),
path('aa_logout/', views.aa_logout, name='aa_logout'),
path('upload_file/', views.upload_file, name='upload_file'),
path('files/', views.files, name='files'),
path('delete/<int:pk>/', views.delete, name='delete'),
path('search_file/', views.search_file, name='search_file'),
path('all_users/', views.all_users, name='all_users'),
path('send_request/<int:pk>/', views.send_request, name='send_request'),
path('requested_file/', views.requested_file, name='requested_file'),
path('send_key/', views.send_key, name='send_key'),
path('generate_aakey/<int:pk>/', views.generate_aakey, name='generate_aakey'),
path('download_file/<int:pk>/', views.download_file, name='download_file'),
path('view_keys/<int:pk>/', views.view_keys, name='view_keys'),
path('add_keyword/', views.add_keyword, name='add_keyword')
]