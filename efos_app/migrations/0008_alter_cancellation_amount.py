# Generated by Django 4.2.5 on 2023-10-16 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('efos_app', '0007_rename_art74reductions_art74reduction_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cancellation',
            name='amount',
            field=models.DecimalField(decimal_places=3, max_digits=12),
        ),
    ]