from rest_framework import generics, serializers, filters
from accounts.permissions import IsAdministrator
from .models import Patient


# Serializer shu yerning o'zida
class PatientListSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source='user.get_full_name')
    email = serializers.EmailField(source='user.email')
    phone = serializers.CharField(source='user.tel_number')

    class Meta:
        model = Patient
        fields = ['id', 'registration_number', 'full_name', 'email', 'phone', 'condition']


class PatientListView(generics.ListAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientListSerializer
    permission_classes = [IsAdministrator]

    # Pagination — sahifa boshiga 10 ta
    pagination_class = None  # pastda settings.py orqali sozlanadi

    # Qidiruv — registratsiya raqami bo'yicha
    filter_backends = [filters.SearchFilter]
    search_fields = ['registration_number']