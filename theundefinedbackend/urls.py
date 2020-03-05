"""theundefinedbackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api import views
from api.views import login
from undefined_world_rooms.views import RoomViewSet
from undefined_world_players.views import PlayerViewSet

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'rooms', RoomViewSet)
router.register(r'players', PlayerViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login', login),  
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('rooms/', include('undefined_world_rooms.urls')),
    path('players/', include('undefined_world_players.urls'))
]
