# Generated by Django 5.0.6 on 2024-06-03 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0007_rename_category_itemcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemcategory',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='category_of_item/'),
        ),
    ]
