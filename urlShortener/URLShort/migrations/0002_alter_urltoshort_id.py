# Generated by Django 4.0.4 on 2022-05-04 15:11

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('URLShort', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urltoshort',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
