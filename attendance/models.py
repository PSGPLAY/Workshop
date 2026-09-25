from django.db import models

# Create your models here.
from students.models import Enrollment, Student
from courses.models import Course

class Attendance(models.Model):
   STATUS_CHOICE=[
      ("present", "Present"),
      ("absent", "Absent"),
      ("late", "Late"),
   ]

   student = models.ForeignKey(Student, on_delete=models.CASCADE,related_name="attendance_records")

   course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="attendance_records")

   date = models.DateField()

   status = models.CharField(max_length=10, choices=STATUS_CHOICE, default="absent")

   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)

   class Meta:
      constraints = [models.UniqueConstraint(fields=["student", "course", "date"],name="unique_student_course_attendance")]

      def __str__(self):
        return f"{self.student} - {self.course} - {self.date}"