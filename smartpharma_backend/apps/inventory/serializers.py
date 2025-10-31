from rest_framework import serializers
from .models import Inward, Outward, StockStatement

class InwardSerializer(serializers.ModelSerializer):
    item_name = serializers.CharField(source='item.name', read_only=True)
    vendor_name = serializers.CharField(source='vendor.name', read_only=True)

    class Meta:
        model = Inward
        fields = '__all__'

class OutwardSerializer(serializers.ModelSerializer):
    item_name = serializers.CharField(source='item.name', read_only=True)

    class Meta:
        model = Outward
        fields = '__all__'

class StockStatementSerializer(serializers.ModelSerializer):
    item_name = serializers.CharField(source='item.name', read_only=True)
    item_code = serializers.CharField(source='item.code', read_only=True)

    class Meta:
        model = StockStatement
        fields = '__all__'