# Generated by Django 5.0.6 on 2024-06-03 08:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rentalitem',
            name='category',
        ),
        migrations.AddField(
            model_name='rentalitem',
            name='Category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rental_items', to='items.category'),
        ),
    ]
