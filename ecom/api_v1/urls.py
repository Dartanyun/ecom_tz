from api_v1.views.users import UsersViewSet
from django.urls import include, path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("users", UsersViewSet, basename="users")

urlpatterns = [
    path("v1/", include(router.urls)),
    path("auth/", include("djoser.urls.authtoken")),
]
