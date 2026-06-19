from rest_framework import generics, serializers, status
from rest_framework.response import Response
from accounts.permissions import IsAdministrator
from accounts.models import User
from .models import Doctor


class DoctorCreateSerializer(serializers.Serializer):
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField()
    tel_number = serializers.CharField()
    first_name = serializers.CharField(required=False, allow_blank=True)
    last_name = serializers.CharField(required=False, allow_blank=True)
    specialization = serializers.CharField()
    procedure_cost = serializers.DecimalField(max_digits=10, decimal_places=2)

    def create(self, validated_data):
        # 1. Avval User yaratamiz
        user = User.objects.create_user(
            username=validated_data['email'],   # email'ni username qilib ishlatamiz
            email=validated_data['email'],
            password=validated_data['password'],
            tel_number=validated_data['tel_number'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            role='Doctor',
        )
        # 2. Keyin Doctor profilini yaratamiz
        doctor = Doctor.objects.create(
            user=user,
            specialization=validated_data['specialization'],
            procedure_cost=validated_data['procedure_cost'],
        )
        return doctor


class DoctorCreateView(generics.CreateAPIView):
    serializer_class = DoctorCreateSerializer
    permission_classes = [IsAdministrator]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        doctor = serializer.save()
        return Response(
            {'message': 'Shifokor yaratildi', 'doctor_id': doctor.id},
            status=status.HTTP_201_CREATED
        )