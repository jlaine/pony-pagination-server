from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework import generics

from .models import Pony
from .serializers import PonySerializer


class PonyList(generics.ListAPIView):
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_fields = ("is_available",)
    queryset = Pony.objects.all()
    search_fields = ("name",)
    serializer_class = PonySerializer
