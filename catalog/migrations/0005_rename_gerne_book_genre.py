# Generated by Django 4.1.5 on 2023-01-30 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_rename_genre_book_gerne'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='gerne',
            new_name='genre',
        ),
    ]
