from datetime import datetime
from django.db.models import Sum

def check_low_stock_items(items, reorder_level):
    """Check which items are below reorder level"""
    low_stock = []
    for item in items:
        if item.quantity <= reorder_level:
            low_stock.append({
                'id': item.id,
                'name': item.name,
                'current_stock': item.quantity,
                'reorder_level': reorder_level
            })
    return low_stock

def generate_batch_number():
    """Generate unique batch number"""
    from ..common_helpers import generate_unique_code
    prefix = f"BATCH{datetime.now().strftime('%Y%m')}"
    return generate_unique_code(prefix=prefix)

def calculate_stock_value(items):
    """Calculate total stock value"""
    total_value = sum(item.quantity * item.purchase_rate for item in items)
    return total_value

def update_stock_statement(item):
    """Update stock statement for an item"""
    from apps.inventory.models import StockStatement
    
    inward_total = item.inward_set.aggregate(total=Sum('quantity'))['total'] or 0
    outward_total = item.outward_set.aggregate(total=Sum('quantity'))['total'] or 0
    closing_stock = inward_total - outward_total
    
    stock_statement, created = StockStatement.objects.get_or_create(
        item=item,
        defaults={
            'inward_total': inward_total,
            'outward_total': outward_total,
            'closing_stock': closing_stock
        }
    )
    
    if not created:
        stock_statement.inward_total = inward_total
        stock_statement.outward_total = outward_total
        stock_statement.closing_stock = closing_stock
        stock_statement.save()
    
    return stock_statement