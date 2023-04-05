from rest_framework import viewsets, mixins, generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Employee, Department
from .serializers import EmployeeSerializer, DepartmentSerializer
from rest_framework.pagination import PageNumberPagination


class EmployeeViewSet(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      viewsets.GenericViewSet):
    """api для списка сотрудников(только для авторизованных, пагинация) + фильтр для поиска по фамилии и по id департамента"""
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['department']
    search_fields = ['lastname']
    pagination_class = PageNumberPagination

class DepartmentViewSet(generics.ListAPIView):
    """api для получения списка департаментов с суммарным окладом и количеством сотрудников"""
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [permissions.IsAuthenticated]

