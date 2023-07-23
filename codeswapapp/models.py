from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    email = models.EmailField()
    query = models.TextField()

    def __str__(self):
        return self.name
    

class ProductQuery(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
