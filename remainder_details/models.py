from django.db import models
import uuid 
from safedelete.models import SafeDeleteModel
from safedelete import SOFT_DELETE_CASCADE


# Create your models here.

class RemainderDetails(models.Model):
    _safedelete_policy = SOFT_DELETE_CASCADE   # if data was deleted,then it would be stored in db

    REMAINDER_TYPE =( 
        ("1", "Sms"), 
        ("2", "Email"), 
       
    ) 

    id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    date = models.DateField(null=True)
    time = models.TimeField(blank=True)
    remainder_type = models.CharField(max_length=1,choices=REMAINDER_TYPE)
    description = models.TextField(blank=True)