from django.db import models
from user import models as usermodel
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Detail(models.Model):
    time = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    volunteer = models.OneToOneField(usermodel.User,on_delete=models.PROTECT)
    about = RichTextUploadingField()

    
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
    details = models.ForeignKey(Detail,on_delete=models.CASCADE,blank=True,null=True)

