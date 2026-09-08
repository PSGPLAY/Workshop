from rest_framework import serializers
from students.models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [
            "id",
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
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
        ]

    def validate_email(self, value):
        student_id = self.instance.id if self.instance else None

        if Student.objects.filter(email=value).exclude(id=student_id).exists():
            raise serializers.ValidationError(
                "A student with this email already exists."
            )

        return value