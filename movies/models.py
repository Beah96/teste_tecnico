import uuid
from django.db import models

class FavoriteMovie(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    movie = models.IntegerField()
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)