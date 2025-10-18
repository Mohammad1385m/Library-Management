from django.db import models


# Create your models here.

class BorrowersModel(models.Model):
    name = models.CharField()
    email = models.EmailField()
    phone = models.CharField()
    address = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.email}"

    def show_name(self):
        return self.name
