from django.urls import path 
from tasks.views import TaskDetailAPIView, TaskListAPIView 
from. import views

urlpatterns = [ 
    path('tasks/', views.TaskListAPIView.as_view()),
    path('tasks/<int:pk>/', views.TaskDetailAPIView.as_view()),
]