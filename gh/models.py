from django.db import models

# Create your models here.
from django.contrib.auth import get_user_model
from django.db import models

class Profile(models.Model):
  user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
  token = models.TextField()

  def __str__(self):
    return f"Profile for {self.user.username}"
    