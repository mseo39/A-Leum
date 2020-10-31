from django.db import models
from user import models as usermodel


# Create your models here.


    
class Disabled(models.Model):
    name = models.CharField(max_length=50)
    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_CHOICES = (
        (GENDER_MALE,"male"),
        (GENDER_FEMALE,"female")
    )
    gender = models.CharField(max_length = 10,choices=GENDER_CHOICES)
    age = models.IntegerField(default=0)
    handicap_type = models.CharField(max_length = 50)

    #details = models.ForeignKey(Detail,blank=True,null=True)

class Detail(models.Model):
    time = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    volunteer_name = models.CharField(max_length = 50)
    #volunteer = models.ForeignKey(usermodel.User,on_delete=models.PROTECT)
    about = models.TextField(null=True,blank=True)
    disabled = models.ForeignKey(Disabled,on_delete=models.CASCADE,null=True,blank=True)
    #volunteer = models.ForeignKey(usermodel.User,on_delete=models.PROTECT)

