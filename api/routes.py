from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import OrganizationViewSet

routers = DefaultRouter()
routers.register("orgs", OrganizationViewSet, basename="orgs")

urlpatterns = [path("", include(routers.urls))]
