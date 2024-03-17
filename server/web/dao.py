from .models import User, Category, Course
from django.db.models import Count


def load_users():
    return User.objects.filter(is_active=True).all()


def load_categories():
    return Category.objects.filter(active=True).all()


def load_courses(params={}):
    data = Course.objects.filter(active=True).all()

    keyword = params.get('keyword')
    if keyword:
        data = data.filter(name__icontains=keyword)

    category_id = params.get('category_id')
    if category_id:
        data = data.filter(category_id=category_id)

    return data


def load_amount_courses():
    return Category.objects.annotate(amount=Count('course__id')).values("id", "name", "amount").all()