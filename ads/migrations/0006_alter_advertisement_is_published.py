# Generated by Django 4.1.6 on 2023-03-13 07:17

import ads.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0005_alter_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='is_published',
            field=models.BooleanField(validators=[ads.validators.check_is_published]),
        ),
    ]
