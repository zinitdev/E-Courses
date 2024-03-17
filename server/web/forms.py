from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Course


class CourseAdminForm(forms.ModelForm):
    desciption = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Course
        fields = '__all__'