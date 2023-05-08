from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

class Author(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('authors_detail_url_nickname', kwargs={'pk': self.id})