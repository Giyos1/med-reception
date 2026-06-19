from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    # Standart username maydonini phone_number ga almashtiramiz
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields[self.username_field] = serializers.CharField()

    def validate(self, attrs):
        # attrs ichidagi phone_number ni Django authenticate tushunishi uchun username ga tenglaymiz
        password = attrs.get("password")
        phone_number = attrs.get(self.username_field)

        user = authenticate(request=self.context.get('request'), phone_number=phone_number, password=password)

        if not user:
            raise serializers.ValidationError("Telefon raqam yoki parol xato.")

        if not user.is_active:
            raise serializers.ValidationError("Foydalanuvchi faol emas.")

        # Standart access va refresh tokenlarni olish
        data = super().validate(attrs)

        # Response ga foydalanuvchi rolini qo'shish
        data['role'] = user.role
        return data
