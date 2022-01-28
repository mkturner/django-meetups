from django.db import models

# Create your models here.
# class representations of the data that will be handled
# django will use ORM to create & manipulate SQL representations (migrations)
# MAKE SURE app is declared in settings.INSTALLED_APPS 
# before attempting to makemigrations
# inherit from models.Model base class


# Meet Model
class Meet(models.Model):
    # define the columns this model will have and their data types

    # CharField for short-form text
    title = models.CharField(max_length=255)

    # SlugField enforces web-safe slug format, no whitespace
    # unique=True makes sure no repeated values
    # also creates index to make slug queries more effiecient
    slug = models.SlugField(unique=True)

    # TextField is long-form alternative to CharField
    description = models.TextField()

    location = models.CharField(max_length=64)

    # ImageField allows uploading uploading images
    # Django will upload the image and store the path for you
    # Does not store the blob in db
    # 'upload_to=<folder>' param tells Django path to store images under
    # this functionality has a dependency on Pillow, verify it is installed!
    # also, set MEDIA_ROOT, MEDIA_URL in settings.py
    image = models.ImageField(upload_to='images')

    # important to define dunder str, will be used in admin site
    def __str__(self):
        return f"{self.title} meetup"
    
    def __repr__(self):
        return f"{self.title} in {self.location}"