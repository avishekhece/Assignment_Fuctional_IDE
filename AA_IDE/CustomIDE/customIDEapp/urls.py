import views
from django.urls import path
from . import views
from .views import ExecutionList

urlpatterns = [
    path("", views.index, name="index"),
    path('execute/', views.CodeExecutor.as_view(), name='execute_code'),
    path('executions/', ExecutionList.as_view(), name='execution-list'),
]