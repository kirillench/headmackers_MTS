from django.db import models

class OrganizationalMember(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.name} {self.surname} ({self.position})"

    class Meta:
        verbose_name = "Член организации"
        verbose_name_plural = "Члены организации"

