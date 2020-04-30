from django.db import models
from django.urls import reverse


class TodoItem(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_update_url(self):
        return reverse('todo_update_view', kwargs={'todo_id': self.id})

    def get_delete_url(self):
        return reverse('todo_delete_view', kwargs={'todo_id': self.id})
