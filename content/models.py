from django.db import models
from django.utils import timezone
from tinymce import models as tinymce_models
from django.utils.safestring import mark_safe
# Create your models here.


class Header(models.Model):
    background_image = models.ImageField(blank=True, null=True)
    title = models.CharField(blank=True, null=True, max_length=100)
    subtitle = models.CharField(blank=True, null=True, max_length=100)
    link = models.URLField(
        max_length=200, help_text="Please enter a link for learn more button", blank=True, null=True)
    button_text = models.CharField(
        blank=True, null=True, max_length=100, default="Learn More")
    link2 = models.URLField(max_length=200, blank=True, null=True,
                            help_text="Please enter a link for learn more button", )
    button_text2 = models.CharField(
        blank=True, null=True, max_length=100, default="Learn More")

    def __str__(self):
        return self.title

class SubHeader(models.Model):
    title = models.CharField(blank=True, null=True, max_length=100)
    subtitle = models.TextField(blank=True, null=True)
    link = models.URLField(
        max_length=200, help_text="Please enter a link for learn more button", blank=True, null=True)
    button_text = models.CharField(
        blank=True, null=True, max_length=100, default="Learn More")

    def __str__(self):
        return self.title

class HomeIcon(models.Model):
    title = models.CharField(blank=True, null=True, max_length=100)
    text = models.CharField(blank=True, null=True, max_length=100)
    icon = models.CharField(blank=True, null=True, max_length=100, default="fa-heart", help_text=mark_safe(
        "Please write in which icon you'd like, ie fa-phone. Check <a href='http://fontawesome.io/icons/'>here</a> for icons."))

    def __str__(self):
        return self.title


class CarouselImage(models.Model):
    image = models.ImageField(blank=True, null=True,
                                       help_text="this will be a sliding images on the homepage")
    title = models.CharField(blank=True, null=True, max_length=100)
    carousel_text = models.CharField(blank=True, null=True, max_length=100)

    def __str__(self):
        return self.title

# class SmallImage(models.Model):
#     image = models.ImageField(blank=True, null=True,
#                                        help_text="small rounded image on homepage")
#     title = models.CharField(blank=True, null=True, max_length=100)
#     subtitle = models.CharField(blank=True, null=True, max_length=100)
#     text = models.CharField(blank=True, null=True, max_length=300)

#     def __str__(self):
#         return self.title

