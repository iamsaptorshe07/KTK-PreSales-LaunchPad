from django.db import models
import math
# Create your models here.

class ReferenceCapacity(models.Model):
    LEVEL_CHOICE = (
        ('Easy','Easy'),
        ('Medium','Medium'),
        ('Complex','Complex'),
        ('Very Complex','Very Complex')
    )
    
    object_type = models.CharField(max_length=100, null=False, blank=False)
    level = models.CharField(max_length=50,choices=LEVEL_CHOICE)
    per_hour_capacity = models.FloatField(null=False,blank=False)

    @property
    def required_days(self):
        """Ceil division of hours / per_hour_capacity"""
        if self.per_hour_capacity and self.per_hour_capacity > 0:
            return math.ceil(8 / self.per_hour_capacity)
        return 0
    # Admin Panel view
    def __str__(self):
        return f"{self.object_type} | {self.level} | {self.per_hour_capacity}"
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['object_type', 'level'], name='unique_objectType_level')
        ]


class InfraSetUpReference(models.Model):
    options_methods = (
        ('Terraform','Terraform'),
        ('Manual','Manual'),
        ('YAML','YAML'),
        ('Other','Other')
    )
    object_type = models.CharField(max_length=100)
    method = models.CharField(max_length=50,choices=options_methods)
    hour_for_one_object= models.IntegerField()
    additional_complexity_hour = models.IntegerField()
    
    
    def __str__(self):
        return f"{self.object_type} | {self.method} | {self.hour_for_one_object} | {self.additional_complexity_hour}"
    
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['object_type','method'],name='objectType_method')
        ]