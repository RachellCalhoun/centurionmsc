from django.shortcuts import render
from .models import Header, HomeIcon, CarouselImage, SubHeader
from blog.models import Event, Post
from django.utils import timezone

# Create your views here.
def home(request):
    header = Header.objects.all()
    carousel_image = CarouselImage.objects.all()
    icons = HomeIcon.objects.all()
    subhead = SubHeader.objects.all()
    event = Event.objects.filter(start_time__gte=timezone.now()).order_by('start_time')[0]
    
    blog = Post.objects.filter(published_date__lte=timezone.now())[:2]
    return render(request, 'content/home.html', {'header': header, 'blog': blog, 'event': event, 'subhead': subhead, 'carousel_image': carousel_image, 'icons': icons})
