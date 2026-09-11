from django import forms

from .models import Student, Enrollment
from courses.models import Course


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student

        fields = [
            "student_id",
            "first_name",
            "last_name",
            "email",
            "phone",
            "date_of_birth",
            "department",
            "program",
            "semester",
            "status",
            "address",
            "notes",
        ]

        widgets = {
            "student_id": forms.TextInput(
                attrs={
                    "class": "form-input",
                    "placeholder": "e.g. STU-2026-001",
                }
            ),

            "first_name": forms.TextInput(
                attrs={
                    "class": "form-input",
                    "placeholder": "e.g. Emily",
                }
            ),

            "last_name": forms.TextInput(
                attrs={
                    "class": "form-input",
                    "placeholder": "e.g. Carter",
                }
            ),

            "email": forms.EmailInput(
                attrs={
                    "class": "form-input",
                    "placeholder": "e.g. emily.carter@example.com",
                }
            ),

            "phone": forms.TextInput(
                attrs={
                    "class": "form-input",
                    "placeholder": "e.g. +1 555 123 4567",
                }
            ),

            "date_of_birth": forms.DateInput(
                attrs={
                    "class": "form-input",
                    "type": "date",
                }
            ),

            "department": forms.TextInput(
                attrs={
                    "class": "form-input",
                    "placeholder": "e.g. Computer Science",
                }
            ),

            "program": forms.TextInput(
                attrs={
                    "class": "form-input",
                    "placeholder": "e.g. BSc Computer Science",
                }
            ),

            "semester": forms.Select(
                attrs={
                    "class": "form-input",
                }
            ),

            "status": forms.Select(
                attrs={
                    "class": "form-input",
                }
            ),

            "address": forms.Textarea(
                attrs={
                    "class": "form-input",
                    "placeholder": "Student's current address…",
                    "rows": 4,
                }
            ),

            "notes": forms.Textarea(
                attrs={
                    "class": "form-input",
                    "placeholder": "Additional notes about the student…",
                    "rows": 4,
                }
            ),
        }


class EnrollmentForm(forms.ModelForm):

    class Meta:
        model = Enrollment

        fields = [
            "course",
            "status",
        ]

        widgets = {
            "course": forms.Select(
                attrs={
                    "class": "form-input",
                }
            ),

            "status": forms.Select(
                attrs={
                    "class": "form-input",
                }
            ),
        }

    def __init__(self, *args, student=None, **kwargs):

        super().__init__(*args, **kwargs)

        if student:

            enrolled_courses = student.enrollments.values_list(
                "course_id",
                flat=True
            )

            self.fields["course"].queryset = Course.objects.exclude(
                id__in=enrolled_courses
            )
