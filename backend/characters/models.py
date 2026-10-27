from django.db import models


class Character(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    powers = models.TextField()

    image_ref = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    category = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name
