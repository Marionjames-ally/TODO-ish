import datetime as dt
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from cloudinary.models import CloudinaryField

# Create your models here.
class Category(models.Model):
    event_category = models.CharField(max_length = 60, default = 'category')

    def __str__(self):
        return self.event_category

    @classmethod
    def search_category(cls,search_term):
        category = cls.objects.get(event_category__icontains=search_term)
        return category

    @classmethod
    def del_category(cls, id):
        cls.objects.filter(id = id).delete()
    

class Profile(models.Model):
    name = models.CharField(max_length=60)
    bio = models.CharField(max_length=300)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = CloudinaryField('image')
    event_category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} Profile'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


    def create_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()


class Event(models.Model):
    
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    postDate = models.DateTimeField(auto_now_add=True)
    completeDate = models.DateField(null=True)
    time = models.TimeField()
    end_time = models.TimeField(null=True)
    user=models.ForeignKey(Profile,on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


    def create_event(self):
        self.save()
    
    def delete_event(self):
        self.delete()

    def update_event(self):
        self.update()

