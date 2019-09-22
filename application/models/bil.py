from django.db import models
from application.models.lc import LC


class BIL(models.Model):
    bil_number = models.CharField(max_length=100, unique=True, verbose_name='BIL number')
    lc = models.ForeignKey(LC, on_delete=models.CASCADE, related_name='bils')
    shipping_name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        ordering = ["-created"]
        verbose_name_plural = "BILs"

    def __str__(self):
        return self.bil_number
