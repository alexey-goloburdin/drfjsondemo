from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'mymodel', views.MyModelViewSet, basename="MyModel")


urlpatterns = [
    path('', include(router.urls)),
]
