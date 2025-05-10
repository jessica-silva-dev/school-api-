from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import AssessmentSerializer, CourseSerializer
from .models import Assessment, Course

class AssessmentApiView(APIView):
    
    def get(self, request):
        assessment = Assessment.objects.all()
        serializer = AssessmentSerializer(assessment, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

