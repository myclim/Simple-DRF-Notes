from django.db import models
from django.core.validators import MaxLengthValidator



class Note(models.Model):
    title = models.CharField(max_length=200, verbose_name='title')
    content = models.TextField(validators=[MaxLengthValidator(1000),], verbose_name='content')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='created_at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='update_at')

    class Meta:
        verbose_name = 'Note'
        verbose_name_plural = 'Notes'
        ordering = ['-created_at',]

    def __str__(self):
        return self.title[:50]