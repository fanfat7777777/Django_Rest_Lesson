from django.db import models

class AuthorModel(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    birthday_year = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.last_name} | {self.first_name} | {self.birthday_year}'

class BiographyModel(models.Model):
    text = models.TextField()
    author = models.OneToOneField(AuthorModel, on_delete=models.CASCADE)

class BookModel(models.Model):
    name = models.CharField(max_length=64)
    author = models.ManyToManyField(AuthorModel)

    def __str__(self):
        return self.name