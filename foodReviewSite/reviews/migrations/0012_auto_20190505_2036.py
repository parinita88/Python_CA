# Generated by Django 2.1.7 on 2019-05-05 12:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0011_auto_20190504_0123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.DecimalField(decimal_places=1, default=0.0, max_digits=2, validators=[django.core.validators.MaxValueValidator(5.0), django.core.validators.MinValueValidator(0.1)]),
        ),
    ]