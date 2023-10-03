# Generated by Django 4.2.5 on 2023-10-01 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('efos_app', '0003_alter_efo_rfc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persondetail',
            name='assumption',
            field=models.CharField(blank=True, choices=[('FIRMES', 'Firme'), ('EXIGIBLES', 'Exigible'), ('NO LOCALIZADO', 'No Localizado')], max_length=13),
        ),
    ]