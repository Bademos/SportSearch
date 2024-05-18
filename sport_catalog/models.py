from django.db import models
from django.urls import reverse
import uuid
from django.contrib.auth.models import User
from django.conf import settings
 
from datetime import date

class SportUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, help_text = "enter first name" )
    last_name = models.CharField(max_length=100, help_text = "enter last name" )
    isSportsMen = models.BooleanField()
    isManager = models.BooleanField()

    def get_absolute_url(self):
        """
        Returns the url to access a sportuser
        """
        return reverse('sportuser-detail', args=[str(self.id)])
    
    def __str__(self):
        #"""
        #String for representing the Model object (in Admin site etc.)
        #"""
        return self.user.get_username()



class SportType(models.Model):
    """
    Model representing a book genre (e.g. Science Fiction, Non Fiction).
    """
    type_name = models.CharField(max_length=200, help_text="Enter a sport type")

    def __str__(self):
        #"""
        #String for representing the Model object (in Admin site etc.)
        #"""
        return self.type_name


class ProcessingStatus(models.Model):
    description = models.CharField(max_length=50, help_text="Enter status of process")
    def __str__(self):
        return self.description


class Event(models.Model):
    """
    Model representing a specific copy of a book (i.e. that can be borrowed from the library).
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID of event")
    sport_type =  models.ForeignKey(SportType, on_delete=models.SET_NULL, null=True, blank=True)
    manager =  models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    date= models.DateField(null=True, blank=True)
    time= models.TimeField(null=True, blank=True)
    address = models.CharField(max_length=50, help_text="Enter address")
    comment = models.TextField(max_length=500, help_text="Enter comment")
    isClosed = models.BooleanField()
    def __str__(self):
        return '%s (%s)' % (self.id,self.manager)
    
    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        return reverse('event-detail', args=[str(self.id)])


#class ReceiverOfReview(models.Model):
 #   reciever =  models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
  #  def __str__(self):
   #     return '%s' % (self.reciever)



#class SenderOfReview(models.Model):
 #   sender =  models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
  #  def __str__(self):
   #     return '%s' % (self.sender)

class Review(models.Model):
    reciever =  models.ForeignKey(SportUser,on_delete=models.CASCADE, related_name="rcv")
    sender =  models.ForeignKey(SportUser,on_delete=models.CASCADE, related_name="snd")

    #sender =  models.ForeignKey(SenderOfReview, on_delete=models.SET_NULL, null=True, blank=True)
    mark = models.IntegerField()
    comment = models.TextField(max_length=500, help_text="Enter review comment")
    reply = models.TextField(max_length=500, help_text="Enter review comment`s reply")
    isActive = models.BooleanField()
    event =  models.ForeignKey(Event, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return "review on  %s by %s" % (self.event, self.reciever)
    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        return reverse('review-detail', args=[str(self.id)])

class Complaint(models.Model):
    moderator =  models.ForeignKey(SportUser, on_delete=models.SET_NULL, null=True, blank=True)
    review =  models.ForeignKey(Review, on_delete=models.SET_NULL, null=True, blank=True)
    status =  models.ForeignKey(ProcessingStatus, on_delete=models.SET_NULL, null=True, blank=True)
    comment = models.TextField(max_length=500, help_text="Enter complaint comment")
    def __str__(self):
        return "complain on %s" % (self.review)

    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        return reverse('complaint-detail', args=[str(self.id)])

class Application(models.Model):
    event =  models.ForeignKey(Event, on_delete=models.SET_NULL, null=True, blank=True)
    spotsman =  models.ForeignKey(SportUser, on_delete=models.SET_NULL, null=True, blank=True)
    status =  models.ForeignKey(ProcessingStatus, on_delete=models.SET_NULL, null=True, blank=True)
    comment = models.TextField(max_length=500, help_text="Enter application comment")
    def __str__(self):
        return "application on %s by %s" % (self.event, self.spotsman)

class UsersSportTypes(models.Model):
    user = models.ForeignKey(SportUser, on_delete=models.SET_NULL, null=True, blank=True)
    sport_type = models.ManyToManyField(SportType, help_text="Select sport types")
    def __str__(self):
        return "%s of %s" % (self.sport_type, self.user)
