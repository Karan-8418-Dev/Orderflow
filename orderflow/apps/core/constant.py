from django.db  import models
class BaseChoices(models.TextChoices):
    
    @classmethod
    def choices(cls):
        return [(choice.name,choice.label) for choice in cls ]