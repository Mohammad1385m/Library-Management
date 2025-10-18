from django.db import models
from datetime import timedelta
from django.utils import timezone
from userApp.models import *


# Create your models here.


class BooksModel(models.Model):
    title = models.CharField()
    author = models.ForeignKey(to="AuthorsModel", on_delete=models.CASCADE)
    isbn = models.CharField()
    # International Standard Book Id
    available_copies = models.IntegerField()

    def __str__(self):
        return f"{self.title} - {self.author.name} - {self.isbn}"

    def show_title(self):
        return self.title


class AuthorsModel(models.Model):
    name = models.CharField()
    nationality = models.CharField()
    birth_date = models.DateField()
    death_date = models.DateField(null=True, blank=True)
    is_alive = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} - {self.nationality}"

    def save(self, *args, **kwargs):
        if self.death_date:
            self.is_alive = False
        super().save(*args, **kwargs)


class BorrowRecordsModel(models.Model):
    book = models.ForeignKey(to="BooksModel", on_delete=models.CASCADE)
    borrower = models.ForeignKey(to=BorrowersModel, on_delete=models.CASCADE)
    borrow_date = models.DateField(auto_now_add=True)
    due_date = models.DateField(null=True, blank=True)
    is_returned = models.BooleanField(default=False)
    returned_at = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.borrower.name} - {self.book.title} - {self.borrow_date} - {self.due_date} - {self.is_returned}"

    def save(self, *args, **kwargs):
        if not self.pk:
            super().save(*args, **kwargs)
            self.due_date = self.borrow_date + timedelta(days=14)
            super().save(update_fields=["due_date"])
        else:
            if self.is_returned and not self.returned_at:
                self.returned_at = timezone.now().date()
            super().save(*args, **kwargs)
