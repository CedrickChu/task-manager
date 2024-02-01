from django.db import models
from django.urls import reverse

class BaseModel(models.Model):
    created_at = models.TimeField(auto_now_add=True)
    updated_at = models.TimeField(auto_now=True)
    class Meta:
        abstract = True

class Task(BaseModel):
    title = models.CharField(max_length=255, null=True, blank=True)
    created_by = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    due_date = models.DateField(blank=True,null=True)
    def get_absolute_url(self):
        return reverse('task-detail', args=[str(self.id)]) 
    
    def __str__(self):
        return self.title

    
