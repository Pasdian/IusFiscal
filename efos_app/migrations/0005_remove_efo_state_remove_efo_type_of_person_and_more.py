# Generated by Django 4.2.5 on 2023-10-01 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('efos_app', '0004_alter_persondetail_assumption'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='efo',
            name='state',
        ),
        migrations.RemoveField(
            model_name='efo',
            name='type_of_person',
        ),
        migrations.AlterField(
            model_name='persondetail',
            name='assumption',
            field=models.CharField(blank=True, choices=[('FIRMES', 'Firme'), ('EXIGIBLES', 'Exigible'), ('NO LOCALIZADOS', 'No Localizado')], max_length=14),
        ),
    ]