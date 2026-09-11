from django.db import models


class Student(models.Model):
    STATUS_CHOICES = [
        ("active", "Active"),
        ("inactive", "Inactive"),
        ("graduated", "Graduated"),
        ("suspended", "Suspended"),
    ]

    SEMESTER_CHOICES = [
        ("Spring 2026", "Spring 2026"),
        ("Fall 2026", "Fall 2026"),
        ("Spring 2027", "Spring 2027"),
        ("Fall 2027", "Fall 2027"),
    ]

    student_id = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=30, blank=True)

    date_of_birth = models.DateField()

    department = models.CharField(max_length=150)
    program = models.CharField(max_length=150)

    semester = models.CharField(max_length=20,choices=SEMESTER_CHOICES)

    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default="active")

    address = models.TextField(blank=True)
    notes = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["last_name", "first_name"]

    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.student_id} - {self.first_name} {self.last_name}"


class Enrollment(models.Model):

    STATUS_CHOICES = [
        ('Enrolled', 'Enrolled'),
        ('Completed', 'Completed'),
        ('Dropped', 'Dropped'),
        ('Withdrawn', 'Withdrawn'),
    ]

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='enrollments'
    )

    course = models.ForeignKey(
        'courses.Course',
        on_delete=models.CASCADE,
        related_name='enrollments'
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Enrolled'
    )

    enrolled_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['student', 'course'],
                name='unique_student_course'
            )
        ]

    def __str__(self):
        return f"{self.student} - {self.course}"
