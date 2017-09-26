from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from tinymce import models as tinymce_models

class Event(models.Model):
    title = models.CharField(max_length=200)
    text = tinymce_models.HTMLField(blank=True, null=True, help_text="Enter a short description.")
    img = models.ImageField(null=True, blank=True)
    poster = models.FileField(null=True, blank=True)
    start_time = models.DateTimeField(default=timezone.now, blank=True, null=True)
    end_time = models.DateTimeField(default=timezone.now, blank=True, null=True)
    link = models.URLField(
        max_length=200, help_text="Please enter a link to register for the event", blank=True, null=True)
    button_text = models.CharField(
        blank=True, null=True, max_length=100, default="Register now")

    def __str__(self):
        return self.title



class Post(models.Model):
    author= models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = tinymce_models.HTMLField(blank=True, null=True, help_text="Enter a short description.")
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    img = models.ImageField(null=True, blank=True)
    
    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.CharField(max_length=200)
    text = tinymce_models.HTMLField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
