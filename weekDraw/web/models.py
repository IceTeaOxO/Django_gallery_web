from django.db import models

# Create your models here.
class User(models.Model):
    user_image = models.ImageField(upload_to='image/%Y/%m/%d/')
    
    
    def __str__(self):
        return self.user_image