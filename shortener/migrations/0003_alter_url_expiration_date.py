# Generated by Django 4.2.1 on 2023-05-26 09:07

from django.db import migrations, models
import shortener.models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0002_remove_url_slug_url_expiration_date_url_hash_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='expiration_date',
            field=models.DateTimeField(default=shortener.models.get_expiration_date),
        ),
    ]
