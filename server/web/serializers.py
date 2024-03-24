from .models import User, Course, Category
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True },
            'url': {'view_name': 'user-detail', 'lookup_field': 'username'}
        }


class CategorySerializer(serializers.HyperlinkedModelSerializer):    
    # url = serializers.HyperlinkedIdentityField(
    #     view_name='category-detail',
    #     lookup_field='slug'
    # )
        
    class Meta:
        model = Category
        fields = '__all__'
        extra_kwargs = {
            'url': {'view_name': 'category-detail', 'lookup_field': 'slug'},
        }

    

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


