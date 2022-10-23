from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .senserValue.views import SensorViewSet
from .users.views import UserViewSet, ManageUserView

router = routers.DefaultRouter()
router.register('users', UserViewSet, basename="User")
router.register('sensorValue', SensorViewSet, basename="Sensor")

urlpatterns = [
    path('myself/', ManageUserView.as_view(), name='myself'),
    # ユーザ名とパスワードをPOSTするとトークンを返す。
    path('', include(router.urls)),
]
