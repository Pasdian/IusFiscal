# Generated by Django 4.2.5 on 2023-10-31 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('efos_app', '0013_alter_persondetail_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='art74reduction',
            name='state',
            field=models.CharField(blank=True, choices=[('AGUASCALIENTES', 'Aguascalientes'), ('BAJA CALIFORNIA', 'Baja California'), ('BAJA CALIFORNIA SUR', 'Baja California Sur'), ('CAMPECHE', 'Campeche'), ('CHIAPAS', 'Chiapas'), ('CHIHUAHUA', 'Chihuahua'), ('CIUDAD DE MEXICO', 'Ciudad De Mexico'), ('COAHUILA DE ZARAGOZA', 'Coahuila'), ('COLIMA', 'Colima'), ('DURANGO', 'Durango'), ('GUANAJUATO', 'Guanajuato'), ('GUERRERO', 'Guerrero'), ('HIDALGO', 'Hidalgo'), ('JALISCO', 'Jalisco'), ('MEXICO', 'Estado de México'), ('MICHOACAN DE OCAMPO', 'Michoacán'), ('MORELOS', 'Morelos'), ('NAYARIT', 'Nayarit'), ('NUEVO LEON', 'Nuevo Leon'), ('OAXACA', 'Oaxaca'), ('PUEBLA', 'Puebla'), ('QUERETARO', 'Queretaro'), ('QUINTANA ROO', 'Quintana Roo'), ('SAN LUIS POTOSI', 'San Luis Potosi'), ('SINALOA', 'Sinaloa'), ('SONORA', 'Sonora'), ('TABASCO', 'Tabasco'), ('TAMAULIPAS', 'Tamaulipas'), ('TLAXCALA', 'Tlaxcala'), ('VERACRUZ DE IGNACIO DE LA LLAVE', 'Veracruz'), ('YUCATAN', 'Yucatan'), ('ZACATECAS', 'Zacatecas')]),
        ),
    ]
