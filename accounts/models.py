from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
import datetime

# Create your models here.

class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete = models.CASCADE)
    user_contact = models.CharField(max_length=15,blank='True',null='True',default=" ")
    team_mate_contact = models.CharField(max_length=15,blank='True',null='True',default=" ")
    team_mate_name = models.CharField(max_length=50,blank='True',null='True',default=" ")
    team_mate_email = models.CharField(max_length=50,blank='True',null='True',default=" ")

    def __str__(self):
        return self.user.first_name


class UserProgress(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    cluedead = models.DateTimeField(null=True, blank=True, default = timezone.now()+datetime.timedelta(days=2))
    clueReached = models.IntegerField(default=1)
    clue1solved = models.DateTimeField(null=True, blank=True)
    clue2solved = models.DateTimeField(null=True, blank=True)
    clue3solved = models.DateTimeField(null=True, blank=True)
    clue4solved = models.DateTimeField(null=True, blank=True)
    clue5solved = models.DateTimeField(null=True, blank=True)
    clue6solved = models.DateTimeField(null=True, blank=True)
    clue7solved = models.DateTimeField(null=True, blank=True)
    clue8solved = models.DateTimeField(null=True, blank=True)
    clue9solved = models.DateTimeField(null=True, blank=True)
    clue10solved = models.DateTimeField(null=True, blank=True)
    clue11solved = models.DateTimeField(null=True, blank=True)
    clue12solved = models.DateTimeField(null=True, blank=True)
    clue13solved = models.DateTimeField(null=True, blank=True)
    clue14solved = models.DateTimeField(null=True, blank=True)
    clue15solved = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.user.first_name

    def updateclue(self):
        if(self.clueReached == 1):
            self.clue1solved = timezone.now()
        elif(self.clueReached == 2):
            self.clue2solved = timezone.now()
        elif(self.clueReached == 3):
            self.clue3solved = timezone.now()
        elif(self.clueReached == 4):
            self.clue4solved = timezone.now()
        elif(self.clueReached == 5):
            self.clue5solved = timezone.now()
        elif(self.clueReached == 6):
            self.clue6solved = timezone.now()
        elif(self.clueReached == 7):
            self.clue7solved = timezone.now()
        elif(self.clueReached == 8):
            self.clue8solved = timezone.now()
        elif(self.clueReached == 9):
            self.clue9solved = timezone.now()
        elif(self.clueReached == 10):
            self.clue10solved = timezone.now()
        elif(self.clueReached == 11):
            self.clue11solved = timezone.now()
        elif(self.clueReached == 12):
            self.clue12solved = timezone.now()
        elif(self.clueReached == 13):
            self.clue13solved = timezone.now()
        elif(self.clueReached == 14):
            self.clue14solved = timezone.now()
        elif(self.clueReached == 15):
            self.clue15solved = timezone.now()
        super(UserProgress,self).save()




@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProgress.objects.create(user=instance)
        UserProfile.objects.create(user=instance)
    
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprogress.save()
    instance.userprofile.save()

class WonUser(models.Model):
    position = models.IntegerField(default=0)
    time_won = models.DateTimeField()
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    username = models.CharField(max_length = 50)
    email = models.CharField(max_length = 50)
    clue1solved  = models.DateTimeField(null='True')
    clue2solved  = models.DateTimeField(null='True')
    clue3solved  = models.DateTimeField(null='True')
    clue4solved = models.DateTimeField(null='True')
    clue5solved = models.DateTimeField(null='True')
    clue6solved = models.DateTimeField(null='True')
    clue7solved = models.DateTimeField(null='True')
    clue8solved = models.DateTimeField(null='True')
    clue9solved = models.DateTimeField(null='True')
    clue10solved = models.DateTimeField(null='True')
    clue11solved = models.DateTimeField(null='True')
    clue12solved = models.DateTimeField(null='True')
    clue13solved = models.DateTimeField(null='True')
    clue14solved = models.DateTimeField(null='True')
    clue15solved = models.DateTimeField(null='True')