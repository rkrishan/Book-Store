from __future__ import unicode_literals
from decimal import Decimal
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.

class Catalog(models.Model):
    name = models.CharField(max_length=225)
    author_name = models.SlugField(max_length=150)
    category = models.CharField(max_length=300)
    description = models.TextField()
    pub_date = models.DateTimeField(default=datetime.now)

    def __unicode__(self):
        return self.name

   
	
	





