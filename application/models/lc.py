from django.db import models


class LC(models.Model):
    lc_number = models.CharField(max_length=100, unique=True, verbose_name='LC number')
    issue_bank = models.CharField(max_length=100)
    issue_date = models.DateField()
    expire_date = models.DateField()
    client_name = models.CharField(max_length=100)
    client_bank_name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        ordering = ["-created"]
        verbose_name_plural = "LCs"

    def __str__(self):
        return self.lc_number
