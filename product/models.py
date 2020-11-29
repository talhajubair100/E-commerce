from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    parent = models.ForeignKey("self", blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(blank=True ,upload_to='category_image')
    status = models.CharField(max_length=5, choices=STATUS)
    slug = models.SlugField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

   
class Product(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=200)
    category = models.ForeignKey(Category , on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(upload_to='product_image/')
    price = models.DecimalField(max_digits=12, decimal_places=2)
    amount = models.IntegerField()
    minamount=models.IntegerField()
    detail = models.TextField() 
    slug = models.SlugField()
    status = models.CharField(max_length=5,choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title