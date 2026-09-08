from rest_framework.decorators import api_view
from rest_framework.response import Response

from students.models import Student
from .serializers import StudentSerializer


@api_view(["GET"])
def student_list(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)