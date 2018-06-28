from django.shortcuts import render
from django.http import HttpResponse

# def index(request):
#     return HttpResponse("God Loves you.")

# Create your views here.
def prayer_request_list(request):
    return render(request, 'godlovesyouapp/prayer_request_list.html', {})