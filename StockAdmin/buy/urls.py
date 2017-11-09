from django.conf.urls import url

from .views import *

urlpatterns = [
	url(r'^update/(?P<buy_num>[\w-]+)/$', BuyUpdateView.as_view()),
]