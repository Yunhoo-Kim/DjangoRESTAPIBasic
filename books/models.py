from django.db import models


class Book(models.Model):
    title = models.TextField()
    content = models.TextField()
    author_name = models.TextField(help_text="작가 이름이에요.")
    price = models.IntegerField(default=0)

    class Meta:
        db_table = "book"


