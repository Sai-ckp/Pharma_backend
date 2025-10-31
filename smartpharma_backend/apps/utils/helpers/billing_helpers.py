from decimal import Decimal

def calculate_bill_totals(items):
    """Calculate bill totals including tax and discount"""
    subtotal = sum(item['quantity'] * item['rate'] for item in items)
    tax_rate = Decimal('0.18')  # 18% GST
    tax_amount = subtotal * tax_rate
    
    total = {
        'subtotal': subtotal,
        'tax_rate': tax_rate,
        'tax_amount': tax_amount,
        'grand_total': subtotal + tax_amount
    }
    return total

def generate_bill_number():
    """Generate unique bill number with prefix"""
    from datetime import datetime
    from ..common_helpers import generate_unique_code
    
    today = datetime.now()
    prefix = f"BILL{today.strftime('%Y%m')}"
    return generate_unique_code(prefix=prefix)

def validate_bill_items(items, inventory):
    """Validate if items can be billed based on inventory"""
    errors = []
    for item in items:
        stock = inventory.get(item['item_id'])
        if not stock:
            errors.append(f"Item {item['item_id']} not found in inventory")
        elif stock < item['quantity']:
            errors.append(f"Insufficient stock for item {item['item_id']}")
    return errors