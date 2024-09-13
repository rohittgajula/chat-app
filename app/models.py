from django.db import models


class ChatRoom(models.Model):
  name = models.CharField(max_length=150, blank=False, null=False)
  slug = models.SlugField(unique=True)

  def __str__(self):
    return self.name
  
  