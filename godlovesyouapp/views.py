from django.shortcuts import render
from django.http import HttpResponse
from .models import PrayerRequest
from django.utils import timezone
from django.shortcuts import render, get_object_or_404


# def index(request):
#     return HttpResponse("God Loves you.")

# Create your views here.
def prayer_request_list(request):
	print('Heloo there asmlaldanldnlasnd **************')
	prs = PrayerRequest.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'godlovesyouapp/prayer_request_list.html', {'prs':prs})

def prayer_request_detail(request,pk):
	pr = get_object_or_404(PrayerRequest, pk=pk)
	return render(request, 'godlovesyouapp/prayer_request_detail.html', {'pr': pr})