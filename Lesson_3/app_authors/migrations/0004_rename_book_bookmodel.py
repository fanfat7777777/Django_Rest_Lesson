# Generated by Django 3.2.16 on 2023-01-14 03:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_authors', '0003_biographymodel_book'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Book',
            new_name='BookModel',
        ),
    ]
