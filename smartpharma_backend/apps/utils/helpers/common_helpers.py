from datetime import datetime, timedelta
import uuid

def generate_unique_code(prefix='', length=8):
    """Generate a unique code with optional prefix"""
    unique_id = str(uuid.uuid4()).upper()[:length]
    return f"{prefix}{unique_id}"

def calculate_expiry_status(expiry_date):
    """Calculate expiry status of an item"""
    today = datetime.now().date()
    days_until_expiry = (expiry_date - today).days
    
    if days_until_expiry < 0:
        return 'EXPIRED'
    elif days_until_expiry <= 30:
        return 'EXPIRING_SOON'
    elif days_until_expiry <= 90:
        return 'WARNING'
    return 'GOOD'

def format_currency(amount):
    """Format amount to currency string"""
    return f"₹{amount:,.2f}"