from django.db import models
from django.utils import timezone
# Create your models here.


class chai_variety(models.Model):
    CHAI_TYPE_CHOICE = [
        ('ML' , 'MASALA'),
        ('GR' , 'GINGER'),
        ('BT' , 'BLACK'),
        ('KW' , 'KIWI'),
        ('EL' , 'ELAICHI'),
    ]
    
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chais/')
    date_added = models.DateTimeField(default=timezone.now)
    kaisi = models.CharField(max_length=2 , choices = CHAI_TYPE_CHOICE)
    description = models.TextField(default='')
    
    
    def __str__(self):

        return self.name
