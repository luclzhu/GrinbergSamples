from django.urls import path

from . import views
print('hi')
urlpatterns = [
    path('home/', views.home, name = 'home'),
    path('new_sample/', views.new_sample, name = 'new_sample'),
    path('update_sample/<str:pk>/', views.update_sample, name = 'update_sample'),
    path('delete_sample/<str:pk>/', views.delete_sample, name = 'delete_sample'),
    path('new_var/', views.new_var, name = 'new_var'),
    path('update_var/<str:pk>/', views.update_var, name = 'update_var'),
    path('delete_var/<str:pk>/', views.delete_var, name = 'delete_var')
]