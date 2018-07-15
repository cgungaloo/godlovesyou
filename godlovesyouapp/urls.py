from django.urls import path
from django.conf.urls import url
from . import views	

# Put urls in order for page matching

urlpatterns =[
	url(r'^prayer_request_detail/(?P<pk>\d+)/$',views.prayer_request_detail, name='prayer_request_detail'),
	url(r'',views.prayer_request_list, name='prayer_request_list'),
]