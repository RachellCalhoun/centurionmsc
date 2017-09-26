from django.contrib import admin

from .models import Header, HomeIcon, CarouselImage, SubHeader
from django.contrib.flatpages.admin import FlatpageForm, FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from tinymce.widgets import TinyMCE
from django.contrib.sites.models import Site
# Register your models here.



admin.site.register(Header)
admin.site.register(CarouselImage)
admin.site.register(HomeIcon)
admin.site.register(SubHeader)
