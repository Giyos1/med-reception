from rest_framework import mixins, viewsets, status
from rest_framework.response import Response

from .permissions import IsAdministrator
from .serializers import DoctorCreateSerializer


class AdminDoctorViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    permission_classes = [IsAdministrator]
    serializer_class   = DoctorCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {
                "message": "Shifokor muvaffaqiyatli yaratildi.",
                "data":    serializer.data,
            },
            status=status.HTTP_201_CREATED,
        )