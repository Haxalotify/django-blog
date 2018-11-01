from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):#defines our model, object
#Post is the name of the model, models.Model means that Post
#is a django model, so django knows that it should be saved
#in the database
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)#to define text with a limited # of characters
    text = models.TextField()#to enter text
    created_date = models.DateTimeField(default = timezone.now)#for date and time published
    published_date = models.DateTimeField(blank = True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
