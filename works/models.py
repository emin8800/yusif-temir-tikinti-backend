# from django.db import models

# class Work(models.Model):
#     TAB_CHOICES = [
#         ("Sadə-Təmir", "Sadə-Təmir"),
#         ("Skandinav-Təmir", "Skandinav-Təmir"),
#         ("Modern-Təmir", "Modern-Təmir"),
#         ("Loft-Təmir", "Loft-Təmir"),
#         ("Klassik-Təmir", "Klassik-Təmir"),
#         ("Qaba-Tikinti", "Qaba-Tikinti"),
#     ]

#     MEDIA_CHOICES = [
#         ("image", "Image"),
#         ("video", "Video"),
#         ("pdf", "PDF"),
#     ]

#     tab = models.CharField(max_length=50, choices=TAB_CHOICES)
#     title = models.CharField(max_length=200)
#     media_type = models.CharField(max_length=10, choices=MEDIA_CHOICES)

#     file = models.FileField(upload_to="works/")

#     def __str__(self):
#         return self.title

from django.db import models
from cloudinary.models import CloudinaryField

class Work(models.Model):
    TAB_CHOICES = [
        ("Sadə-Təmir", "Sadə-Təmir"),
        ("Skandinav-Təmir", "Skandinav-Təmir"),
        ("Modern-Təmir", "Modern-Təmir"),
        ("Loft-Təmir", "Loft-Təmir"),
        ("Klassik-Təmir", "Klassik-Təmir"),
        ("Qaba-Tikinti", "Qaba-Tikinti"),
    ]

    MEDIA_CHOICES = [
        ("image", "Image"),
        ("video", "Video"),
        ("pdf", "PDF"),
    ]

    tab = models.CharField(max_length=50, choices=TAB_CHOICES)
    title = models.CharField(max_length=200)
    media_type = models.CharField(max_length=10, choices=MEDIA_CHOICES)

    file = CloudinaryField('file')

    def __str__(self):
        return self.title
