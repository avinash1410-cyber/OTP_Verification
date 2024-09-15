from django.db import models
from django.contrib.auth.models import AbstractUser
import random
from django.db import models
from django.utils import timezone







class CustomUser(AbstractUser):
    mobile_number = models.CharField(max_length=15, unique=True)
    is_mobile_verified = models.BooleanField(default=False)
    is_email_verified = models.BooleanField(default=False)





class OTP(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,null=True,blank=True)
    otp_code = models.CharField(max_length=6)
    created_at = models.DateTimeField(default=timezone.now)
    otp_type = models.CharField(max_length=10)  # 'email' or 'mobile'

    def generate_otp(self):
        self.otp_code = ''.join(random.choices('0123456789', k=6))

    def __str__(self):
        return self.otp_code 