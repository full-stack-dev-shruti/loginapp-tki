from django.db import models

class User(models.Model):
    """User class"""

    first_name = models.CharField(
        max_length=255,
    )

    last_name = models.CharField(
        max_length=255,
    )

    email = models.EmailField()

    password = models.CharField(
        max_length=15,
    )