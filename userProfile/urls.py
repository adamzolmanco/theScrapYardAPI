from django.conf.urls import url
from userProfile import views
from django.views.decorators.csrf import csrf_exempt
urlpatterns=[
    url(r'^UserProfile$', csrf_exempt(views.UserProfile)),
    url(r'^UserProfile/([0-9]+)$', views.UserProfile)
]