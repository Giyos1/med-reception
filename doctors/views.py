from rest_framework import mixins, viewsets
from .permissions import IsAdministrator
from .serializers import DoctorCreateSerializer
from .models import Doctor


class AdminDoctorViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    permission_classes = [IsAdministrator]
    serializer_class = DoctorCreateSerializer
    queryset= Doctor.objects.all()