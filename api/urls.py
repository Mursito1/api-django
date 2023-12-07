from django.urls import path, include
from rest_framework import routers
from api import views

router=routers.DefaultRouter()
router.register('usuarios', views.ProfesorViewSet)

urlpatterns=[
    path('', include(router.urls)) 
]