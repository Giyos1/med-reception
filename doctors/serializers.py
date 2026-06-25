from rest_framework import serializers
from users.models import User
from doctors.models import Doctor


class DoctorCreateSerializer(serializers.ModelSerializer):
    phone_number   = serializers.CharField(required=True)
    password       = serializers.CharField(write_only=True, required=True, min_length=8)
    specialization = serializers.CharField(required=True, write_only=True)
    procedure_cost = serializers.DecimalField(required=True, max_digits=10, decimal_places=2, write_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'phone_number',
            'password',
            'first_name',
            'last_name',
            'specialization',
            'procedure_cost',
        ]

    def validate_phone_number(self, value):
        if User.objects.filter(phone_number=value).exists():
            raise serializers.ValidationError("Bu telefon raqami allaqachon ro'yxatdan o'tgan.")
        return value

    def create(self, validated_data):
        specialization = validated_data.pop('specialization')
        procedure_cost = validated_data.pop('procedure_cost')
        password       = validated_data.pop('password')
        phone_number   = validated_data.get('phone_number')

        user = User.objects.create_user(
            username=phone_number,
            phone_number=phone_number,
            password=password,
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            role='shifokor',
        )
        Doctor.objects.create(
            user=user,
            specialization=specialization,
            procedure_cost=procedure_cost,
        )
        return user