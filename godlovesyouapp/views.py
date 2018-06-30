from django.shortcuts import render
from django.http import HttpResponse
from .models import PrayerRequest
from django.utils import timezone

# def index(request):
#     return HttpResponse("God Loves you.")

# Create your views here.
def prayer_request_list(request):
	prs = PrayerRequest.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'godlovesyouapp/prayer_request_list.html', {'prs':prs})