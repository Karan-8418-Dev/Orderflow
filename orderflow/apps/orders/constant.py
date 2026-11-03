from orderflow.apps.core.constant import BaseChoices


class OrderStatus(BaseChoices):
    PENDING = "Pending"
    CONFIRMED = "Confirmed"
    PROCESSING = "Processing"
    SHIPPED = "Shipped"
    DELIVERED = "Delivered"
    CANCELLED = "Cancelled"
    
class IdemPotencyKeysStatus(BaseChoices):
    STARTED ="Started"
    FAILED = "Failed"
    COMPLETED = "COMPLETED"
    
    
ORDER_CHOICES = OrderStatus.choices
IDEMPOTENCY_STATUS_CHOICES = IdemPotencyKeysStatus.choices