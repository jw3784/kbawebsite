from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('alumnus', views.alumnusViewSet)

urlpatterns = [
    path('', views.index, name='alumni'),
    url('^api/', include(router.urls)),
]