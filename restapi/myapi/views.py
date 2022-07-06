from django.shortcuts import render
from rest_framework import viewsets
from .models import Portfolio, Currency
from .serializers import PortfolioSerializer, CurrencySerializer

# Create your views here.


class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all().order_by("title")
    serializer_class = PortfolioSerializer


class CurrencyViewSet(viewsets.ModelViewSet):
    queryset = Currency.objects.all().order_by("symbol")
    serializer_class = CurrencySerializer
