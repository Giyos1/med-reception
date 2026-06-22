from rest_framework import generics, status
from rest_framework.response import Response

from .permissions import IsAdministrator
from .serializers import DoctorCreateSerializer


class AdminDoctorCreateView(generics.CreateAPIView):
    permission_classes = [IsAdministrator]
    serializer_class   = DoctorCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        doctor = serializer.save()
        return Response(
            {
                "message": "Shifokor muvaffaqiyatli yaratildi.",
                "data":    self.get_serializer(doctor).data,
            },
            status=status.HTTP_201_CREATED,
        )