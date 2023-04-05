from django.urls import path
from rest_framework import routers, permissions
from .views2 import EmployeeViewSet, DepartmentViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
router = routers.DefaultRouter()
router.register(r'employees', EmployeeViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Тестовое задание для bvbinfo.ru",
        default_version='v1',
        description="Компания",
        contact=openapi.Contact(email="banzaicool788@gmail.com"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('departments/', DepartmentViewSet.as_view(), name='departments'),
] + router.urls
