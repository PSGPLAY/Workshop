from django import forms
from .models import Course


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = [
            "code",
            "name",
            "department",
            "instructor",
            "credits",
            "duration",
            "semester",
            "capacity",
            "status",
            "description",
        ]

        widgets = {
            "code": forms.TextInput(attrs={"class": "form-input","placeholder": "Enter course code"}),

            "name": forms.TextInput(attrs={"class": "form-input","placeholder": "Enter course name"}),

            "department": forms.TextInput(attrs={"class": "form-input","placeholder": "Enter department"}),

            "instructor": forms.Select(attrs={"class": "form-input"}),

            "credits": forms.NumberInput(attrs={"class": "form-input","min": 1,"placeholder": "Enter credits"}),

            "duration": forms.TextInput(attrs={"class": "form-input","placeholder": "e.g. 16 weeks"}),

            "semester": forms.Select(attrs={"class": "form-input"}),

            "capacity": forms.NumberInput(attrs={"class": "form-input","min": 1,"placeholder": "Enter capacity"}),

            "status": forms.Select(attrs={"class": "form-input"}),

            "description": forms.Textarea(attrs={"class": "form-input","placeholder": "Enter course description","rows": 4}),
        }
