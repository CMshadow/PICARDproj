from __future__ import unicode_literals
from django.contrib import auth
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.timezone import now

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    SEX_CHOICES=(('M','Male'),('F','Female'),('O','Other'))
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, default='M',)
    profile_created = models.BooleanField(default=False)

# class PatientProfile(Profile):
#     ssn = models.CharField(max_length=11, default='000-00-0000')
#     birthday = models.DateField(default=now)
#     weight = models.PositiveIntegerField(null=True)
#     mobilephone = models.CharField(max_length=15,null=True,blank=False)
#     homephone = models.CharField(max_length=15,null=True, blank=True)
#     workphone = models.CharField(max_length=15,null=True, blank=True)
#     fax = models.CharField(max_length=15,null=True, blank=True)
#     address_line = models.CharField(max_length=250, null=True, blank=False)
#     address_city = models.CharField(max_length=50, null=True, blank=False)
#     address_state = models.CharField(max_length=50, null=True, blank=False)
#     address_zip = models.CharField(max_length=5, null=True, blank=False)
#
# class PhysicianProfile(Profile):
#     name = models.CharField(max_length=11, default='000-00-0000')
#
# class CaregiverProfile(Profile):
#     name = models.CharField(max_length=11, default='000-00-0000')

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()




# class UserProfile(models.Model):
# 	user = models.OneToOneField(User)
# 	#addtional attributes
# 	picture = models.ImageField(upload_to ='profile_images',blank=True)
#
# 	def __unicode__(self):
# 		return self.user.username

class Contact(models.Model):
	subject = models.CharField(max_length=50)
	from_email = models.EmailField()
	message = models.CharField(max_length=100)
   	#date_created = models.DateField(verbose_name="Created on date", auto_now_add="True")
	def __unicode__(self):
                return self.message
