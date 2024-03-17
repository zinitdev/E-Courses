from rest_framework import viewsets, generics
from .serializers import UserSerializer, CourseSerializer, CategorySerializer
from .dao import load_users, load_courses, load_categories
from .paginator import LargeResultsSetPagination

class UserViewSet(viewsets.ModelViewSet):
    queryset = load_users()
    serializer_class = UserSerializer


class CategoryViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = load_categories()
    serializer_class = CategorySerializer
    

class CourseViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = load_courses()
    serializer_class = CourseSerializer
    pagination_class = LargeResultsSetPagination