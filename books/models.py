from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.TextField()
    content = models.TextField()
    author_name = models.TextField(help_text="작가 이름이에요.")
    price = models.IntegerField(default=0)

    class Meta:
        db_table = "book"