from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Inward, Outward, StockStatement
from .serializers import InwardSerializer, OutwardSerializer, StockStatementSerializer
from django.db.models import Sum

class InwardViewSet(viewsets.ModelViewSet):
    queryset = Inward.objects.all()
    serializer_class = InwardSerializer

    def perform_create(self, serializer):
        inward = serializer.save()
        # Update stock statement
        stock, created = StockStatement.objects.get_or_create(item=inward.item)
        stock.inward_total += inward.quantity
        stock.closing_stock = stock.inward_total - stock.outward_total
        stock.status = "Sufficient" if stock.closing_stock > inward.item.reorder_level else "Reorder"
        stock.save()

class OutwardViewSet(viewsets.ModelViewSet):
    queryset = Outward.objects.all()
    serializer_class = OutwardSerializer

    def perform_create(self, serializer):
        outward = serializer.save()
        # Update stock statement
        stock, created = StockStatement.objects.get_or_create(item=outward.item)
        stock.outward_total += outward.quantity
        stock.closing_stock = stock.inward_total - stock.outward_total
        stock.status = "Sufficient" if stock.closing_stock > outward.item.reorder_level else "Reorder"
        stock.save()

class StockStatementViewSet(viewsets.ModelViewSet):
    queryset = StockStatement.objects.all()
    serializer_class = StockStatementSerializer
    
@api_view(['GET'])
def stock_summary(request):
    summary = StockStatement.objects.aggregate(
        total_stock=Sum('closing_stock'),
        total_inward=Sum('inward_total'),
        total_outward=Sum('outward_total')
    )
    return Response(summary)