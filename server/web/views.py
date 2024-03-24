from rest_framework import viewsets, generics
from .serializers import UserSerializer, CourseSerializer, CategorySerializer
from .dao import load_users, load_courses, load_categories
from .paginator import LargeResultsSetPagination

class UserViewSet(viewsets.ViewSet, generics.ListAPIView, generics.RetrieveAPIView):
    queryset = load_users()
    serializer_class = UserSerializer
    lookup_field = 'username'


class CategoryViewSet(viewsets.ViewSet, generics.ListAPIView, generics.RetrieveAPIView):
    queryset = load_categories()
    serializer_class = CategorySerializer
    lookup_field = 'slug'


class CourseViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = load_courses()
    serializer_class = CourseSerializer
    pagination_class = LargeResultsSetPagination