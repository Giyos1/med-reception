from rest_framework import serializers
from users.models import User
from .models import Doctor


class DoctorCreateSerializer(serializers.Serializer):
    # User
    phone_number = serializers.CharField(required=True)
    password     = serializers.CharField(write_only=True, required=True, min_length=8)
    first_name   = serializers.CharField(required=False, default='')
    last_name    = serializers.CharField(required=False, default='')

    # Doctor
    specialization = serializers.CharField(required=True)
    procedure_cost = serializers.DecimalField(required=True, max_digits=10, decimal_places=2)

    def validate_phone_number(self, value):
        if User.objects.filter(phone_number=value).exists():
            raise serializers.ValidationError("Bu telefon raqami allaqachon ro'yxatdan o'tgan.")
        return value

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['phone_number'],
            phone_number=validated_data['phone_number'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            role='shifokor',
        )
        doctor = Doctor.objects.create(
            user=user,
            specialization=validated_data['specialization'],
            procedure_cost=validated_data['procedure_cost'],
        )
        return doctor

    def to_representation(self, instance):
        return {
            'id':             instance.id,
            'phone_number':   instance.user.phone_number,
            'first_name':     instance.user.first_name,
            'last_name':      instance.user.last_name,
            'specialization': instance.specialization,
            'procedure_cost': str(instance.procedure_cost),
        }