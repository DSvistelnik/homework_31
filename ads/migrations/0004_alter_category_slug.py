# Generated by Django 4.1.6 on 2023-03-11 07:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0003_category_slug_alter_advertisement_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=200, validators=[django.core.validators.MinLengthValidator(10)]),
        ),
    ]