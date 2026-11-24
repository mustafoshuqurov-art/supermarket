from django.db import models

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=70)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.name

class Product(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    name=models.CharField(max_length=70)
    image=models.ImageField(upload_to="")
    price=models.PositiveIntegerField(default=0)
    description=models.TextField(max_length=500)
  
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
        
    
    def __str__(self):
        return self.name


