from django.urls import path, include
from rest_framework import routers
from api import views

router=routers.DefaultRouter()
router.register('profesores', views.ProfesorViewSet)
router.register('alumnos', views.AlumnoViewSet)

urlpatterns=[
    path('', include(router.urls)) 
]