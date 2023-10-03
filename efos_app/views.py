from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Efo, PersonDetail
from .serializers import PersonSerializer, PersonDetailSerializer
from django.http import Http404
from rest_framework import status, generics, filters


class PersonView(generics.RetrieveAPIView):
    """
    View to get a single person
    """
    queryset = Efo.objects.all()
    serializer_class = PersonSerializer


class SearchPersonView(generics.ListCreateAPIView):
    queryset = Efo.objects.all()
    serializer_class = PersonSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ['rfc']


class PersonDetailView(generics.RetrieveAPIView):
    """
    View to get a single Person Detail
    """
    queryset = PersonDetail.objects.all()
    serializer_class = PersonDetailSerializer


class SearchPersonDetailView(generics.ListCreateAPIView):
    queryset = PersonDetail.objects.all()
    serializer_class = PersonDetailSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ['rfc']
