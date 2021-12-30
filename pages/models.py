from django.db import models

class Teams(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    photo = models.ImageField( upload_to='teams/%Y/%m/%d/')
    facebook_link =models.URLField(max_length=200)
    twitter_link =models.URLField(max_length=200)
    google_link =models.URLField(max_length=200)
    create_at =models.DateTimeField(auto_now_add=True)
    update_at =models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.first_name 
    
    
    
