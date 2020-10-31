from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    """ 커스텀 유저 모델 """

    name = models.CharField(max_length = 50)
    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_CHOICES = (
        (GENDER_MALE,"male"),
        (GENDER_FEMALE,"female")
    )
    gender = models.CharField(max_length = 10,choices=GENDER_CHOICES)
    age = models.IntegerField(default=0)
    phone = models.CharField(max_length = 30)

