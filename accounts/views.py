from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from accounts.serialazer import PatientApplicationSerializer


class PatientRegisterView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = PatientApplicationSerializer
    

    def post(self, request):
        serializer = PatientApplicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
