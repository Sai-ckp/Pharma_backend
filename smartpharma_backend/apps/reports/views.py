from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Sum, Count
from datetime import datetime, timedelta
from apps.billing.models import Bill
from apps.inventory.models import Inward, Outward

@api_view(['GET'])
def sales_report(request):
    start_date = request.query_params.get('start_date', None)
    end_date = request.query_params.get('end_date', None)
    
    queryset = Bill.objects.all()
    if start_date:
        queryset = queryset.filter(date__gte=start_date)
    if end_date:
        queryset = queryset.filter(date__lte=end_date)

    return Response({
        'total_sales': queryset.count(),
        'total_amount': queryset.aggregate(Sum('grand_total'))['grand_total__sum'] or 0,
        'bills': queryset.values('bill_no', 'date', 'grand_total')
    })

@api_view(['GET'])
def inventory_report(request):
    return Response({
        'inward': Inward.objects.values('item__name').annotate(
            total_quantity=Sum('quantity'),
            total_value=Sum('purchase_rate')
        ),
        'outward': Outward.objects.values('item__name').annotate(
            total_quantity=Sum('quantity')
        )
    })