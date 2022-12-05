from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    # path('registrationnewusers/', views.UserRegistration.as_view()),
    path('users/', views.UserList.as_view()),
    path('users//', views.UserDetail.as_view()),
    path('tasks/', views.TaskList.as_view()),
    path('tasks//', views.TaskDetail.as_view()),
    path('responces/', views.ResponsesList.as_view()),
    path('responces//', views.ResponsesDetail.as_view()),
    path('categories/', views.CategoryList.as_view()),
    path('categories//', views.CategoryDetail.as_view()),
    path('universities/', views.UniversityList.as_view()),
    path('universities//', views.UniversityDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)