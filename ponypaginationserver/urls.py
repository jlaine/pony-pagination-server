from django.urls import path

from .views import PonyList


urlpatterns = [
    path('v1/ponies', PonyList.as_view(), name='pony-list'),
]
