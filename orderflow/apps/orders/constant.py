from orderflow.apps.core.constant import BaseChoices


class OrderStatus(BaseChoices):
    PENDING = "Pending"
    CONFIRMED = "Confirmed"
    PROCESSING = "Processing"
    SHIPPED = "Shipped"
    DELIVERED = "Delivered"
    CANCELLED = "Cancelled"
    
    
ORDER_CHOICES = OrderStatus.choices()