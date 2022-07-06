from rest_framework import serializers
from .models import Portfolio, Currency


class PortfolioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Portfolio
        fields = ("id", "title", "description")


class CurrencySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Currency
        fields = (
            "id",
            "name",
            "symbol",
            "price",
            "marketCap",
            "ammount",
            "portfolio",
        )
