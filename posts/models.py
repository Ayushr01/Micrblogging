from django.db import models
from users.models import User

class Post(models.Model):
    """
    Posts Model
    """
    created_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    content = models.TextField(max_length=1000)
    post_date = models.DateTimeField(auto_now_add=True)