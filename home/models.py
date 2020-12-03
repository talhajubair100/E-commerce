from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class Setting(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=255)
    description = models.TextField()
    company = models.CharField(max_length=100)
    address = models.CharField(blank=True,max_length=100)
    phone = models.CharField(blank=True,max_length=15)
    fax = models.CharField(blank=True,max_length=15)
    email = models.EmailField(max_length=254)
    smtpserver = models.CharField(blank=True,max_length=100)
    smtpemail = models.CharField(blank=True,max_length=100)
    smtppassword = models.CharField(blank=True,max_length=100)
    smtpport = models.CharField(blank=True,max_length=15)
    icon = models.ImageField(blank=True,upload_to='product_image/')
    facebook = models.URLField(blank=True, max_length=200)
    instagram = models.URLField(blank=True,max_length=200)
    twitter = models.URLField(blank=True,max_length=200)
    youtube = models.URLField(blank=True, max_length=200)
    aboutus = RichTextUploadingField(blank=True)
    contact = RichTextUploadingField(blank=True)
    references = RichTextUploadingField(blank=True)
    status=models.CharField(max_length=10,choices=STATUS)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Read', 'Read'),
        ('Closed', 'Closed'),
    )
    name= models.CharField(blank=True,max_length=50)
    email= models.EmailField(blank=True, max_length=100)
    subject= models.CharField(blank=True,max_length=100)
    message= models.TextField(blank=True,max_length=255)
    status=models.CharField(max_length=10,choices=STATUS,default='New')
    ip = models.CharField(blank=True, max_length=20)
    note = models.CharField(blank=True, max_length=100)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name