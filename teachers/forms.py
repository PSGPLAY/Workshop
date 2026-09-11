from django import forms
from .models import Teacher


class TeacherForm(forms.ModelForm):
   class Meta:
      model = Teacher

      fields = [
         "teacher_id",
         "subject",
         "first_name",
         "last_name",
         "email",
         "phone",
         "department",
         "position",
         "qualification",
         "experience",
         "joining_date",
         "status",
         "bio",
      ]

      widgets = {

         "teacher_id": forms.TextInput(attrs={"class": "form-input","placeholder": "e.g. STU-2026-001"}),

         "subject": forms.TextInput(attrs={"class":"form-input", "placeholder": "e.g Computer Science"}),
         
         "first_name": forms.TextInput(attrs={"class":"form-input", "placeholder": "e.g Prajwal"}),

         "last_name": forms.TextInput(attrs={"class":"form-input", "placeholder": "e.g Shrestha"}),

         "email": forms.EmailInput(attrs={"class":"form-input", "placeholder": "e.g example@gmail.com"}),

         "phone": forms.TextInput(attrs={"class": "form-input","placeholder": "e.g. 9869696996"}),

         "department": forms.TextInput(attrs={"class": "form-input","placeholder": "e.g. Computer Science"}),

         "position": forms.TextInput(attrs={"class": "form-input","placeholder": "e.g. Professor"}),

         "qualification": forms.TextInput(attrs={"class": "form-input","placeholder": "e.g. PhD in Computer Science"}),

         "experience": forms.NumberInput(attrs={"class": "form-input","placeholder": "e.g. 8","min": "0"}),

         "joining_date": forms.DateInput(attrs={"class": "form-input","type": "date"}),

         "status": forms.Select(attrs={"class": "form-input"}),

         "bio": forms.Textarea(attrs={"class": "form-input","placeholder": "Enter a short biography...","rows": 4}),
      }
