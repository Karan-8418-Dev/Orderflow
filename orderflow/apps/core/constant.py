from django.db  import models
class BaseChoices(models.TextChoices):
    
    @classmethod
    def choices(cls):
        return [(choice.value,choice.label) for choice in cls ]