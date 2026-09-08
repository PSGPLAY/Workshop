from  rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    """Serializer for Student model"""

    class Meta:
        model = Student
        fields = [
            'id',
            'student_id',
            'first_name',
            'last_name',
            'email',
            'phone',
            'date_of_birth',
            'department',
            'program',
            'semester',
            'status',
            'address',
            'notes',
            'created_at',
            'updated_at',
        ]

        read_only_fields = [
            'id',
            'created_at',
            'updated_at',
        ]

    # Custom validation for email
    def validate_email(self, value):
        # When updating an existing student, don't consider
        # that student's own email as a duplicate.
        student_id = self.instance.id if self.instance else None

        if Student.objects.filter(email=value).exclude(id=student_id).exists():
            raise serializers.ValidationError(
                "A student with this email already exists."
            )

        return value