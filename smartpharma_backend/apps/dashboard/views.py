from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Sum, Count
from datetime import date, timedelta
from apps.masters.models import Item
from apps.billing.models import Bill

@api_view(['GET'])
def dashboard_summary(request):
    today = date.today()
    thirty_days_ago = today - timedelta(days=30)

    return Response({
        'inventory_stats': {
            'total_items': Item.objects.count(),
            'low_stock': Item.objects.filter(quantity__lt=models.F('reorder_level')).count(),
            'out_of_stock': Item.objects.filter(quantity=0).count(),
        },
        'sales_stats': {
            'today': Bill.objects.filter(date__date=today).aggregate(
                total=Sum('grand_total'),
                count=Count('id')
            ),
            'month': Bill.objects.filter(date__gte=thirty_days_ago).aggregate(
                total=Sum('grand_total'),
                count=Count('id')
            ),
        },
        'alerts': get_alerts()
    })

def get_alerts():
    alerts = []
    # Check expiring items
    expiring_soon = Item.objects.filter(
        expiry_date__lte=date.today() + timedelta(days=30)
    )
    for item in expiring_soon:
        alerts.append({
            'type': 'expiry',
            'message': f'{item.name} expires on {item.expiry_date}'
        })

    # Check low stock items
    low_stock = Item.objects.filter(quantity__lt=models.F('reorder_level'))
    for item in low_stock:
        alerts.append({
            'type': 'stock',
            'message': f'{item.name} is low on stock ({item.quantity} remaining)'
        })

    return alerts