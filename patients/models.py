from django.db import models
from django.conf import settings


class Patient(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='patient_profile',
        verbose_name='Foydalanuvchi'
    )
    registration_number = models.CharField(
        max_length=20,
        unique=True,
        verbose_name='Registratsiya raqami'
    )
    condition = models.CharField(
        max_length=200,
        blank=True,
        verbose_name='Holati / Kasalligi'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Bemor'
        verbose_name_plural = 'Bemorlar'
        ordering = ['registration_number']

    def __str__(self):
        return f"{self.user.get_full_name()} — {self.registration_number}"

    def save(self, *args, **kwargs):
        # Agar registration_number berilmagan bo'lsa, avtomatik tartib raqami beriladi
        if not self.registration_number:
            last = Patient.objects.order_by('id').last()
            next_id = (last.id + 1) if last else 1
            self.registration_number = str(next_id)
        super().save(*args, **kwargs)