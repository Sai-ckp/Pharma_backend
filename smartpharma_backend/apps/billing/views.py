from rest_framework import viewsets
from apps.utils.helpers.billing_helpers import calculate_bill_totals, generate_bill_number
from apps.utils.helpers.common_helpers import format_currency


class BillViewSet(viewsets.ModelViewSet):
    def create(self, request, *args, **kwargs):
        bill_number = generate_bill_number()
        items = request.data.get('items', [])
        totals = calculate_bill_totals(items)
        
        # Add bill number and calculated totals to request data
        request.data['bill_no'] = bill_number
        request.data['total_amount'] = format_currency(totals['subtotal'])
        request.data['grand_total'] = format_currency(totals['grand_total'])
        
        return super().create(request, *args, **kwargs) 
    
