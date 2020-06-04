from django.urls import path,include
from .views import *

urlpatterns = [
    path('',apiOverview, name= 'apiOverview'),
    path('tasklist/', tasklist, name='tasklist'),
    path('taskDetail/<str:pk>/',taskDetail, name='taskDetail'),
    path('taskCreate/',taskCreate,name='taskCreate'),
    path('taskUpdate/<str:pk>/',taskUpdate, name='taskUpdate'),
    path('taskDelete/<str:pk>/',taskDelete, name='taskDelete'),
]
