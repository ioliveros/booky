# Generated by Django 4.2.15 on 2024-08-16 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='author',
            new_name='author_id',
        ),
    ]
