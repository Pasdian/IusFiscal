# Generated by Django 4.2.5 on 2023-09-30 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Efo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rfc', models.CharField(max_length=13, unique=True)),
                ('social_reason', models.TextField(max_length=250)),
                ('fiscal_situation', models.CharField(choices=[('DEF', 'Definitivo'), ('DES', 'Desvirtuado'), ('PRE', 'Presunto'), ('SFA', 'Sentencia_Favorable')], max_length=3)),
                ('sat_presumtion_date', models.DateField()),
                ('dof_presumtion_date', models.DateField()),
                ('sat_definitive_date', models.DateField()),
                ('dof_definitive_date', models.DateField()),
                ('sat_distorted_date', models.DateField()),
                ('dof_distorted_date', models.DateField()),
                ('sat_favorable_ruling_date', models.DateField()),
                ('dof_favorable_ruling_date', models.DateField()),
                ('sat_presumtion_file_no', models.CharField()),
                ('dof_presumtion_file_no', models.CharField()),
                ('sat_definitive_file_no', models.CharField()),
                ('dof_definitive_file_no', models.CharField()),
                ('sat_distorted_file_no', models.CharField()),
                ('dof_distorted_file_no', models.CharField()),
                ('sat_favorable_ruling_file_no', models.CharField()),
                ('dof_favorable_ruling_file_no', models.CharField()),
                ('sat_presumtion_file_date', models.DateField()),
                ('dof_presumtion_file_date', models.DateField()),
                ('sat_definitive_file_date', models.DateField()),
                ('dof_definitive_file_date', models.DateField()),
                ('sat_distorted_file_date', models.DateField()),
                ('dof_distorted_file_date', models.DateField()),
                ('sat_favorable_ruling_file_date', models.DateField()),
                ('dof_favorable_ruling_file_date', models.DateField()),
                ('state', models.CharField(choices=[('AGUASCALIENTES', 'Aguascalientes'), ('BAJA CALIFORNIA', 'Baja California'), ('BAJA CALIFORNIA SUR', 'Baja California Sur'), ('CAMPECHE', 'Campeche'), ('CHIAPAS', 'Chiapas'), ('CHIHUAHUA', 'Chihuahua'), ('CIUDAD DE MEXICO', 'Ciudad De Mexico'), ('COAHUILA DE ZARAGOZA', 'Coahuila'), ('COLIMA', 'Colima'), ('DURANGO', 'Durango'), ('GUANAJUATO', 'Guanajuato'), ('GUERRERO', 'Guerrero'), ('HIDALGO', 'Hidalgo'), ('JALISCO', 'Jalisco'), ('MEXICO', 'Estado de México'), ('MICHOACAN DE OCAMPO', 'Michoacán'), ('MORELOS', 'Morelos'), ('NAYARIT', 'Nayarit'), ('NUEVO LEON', 'Nuevo Leon'), ('OAXACA', 'Oaxaca'), ('PUEBLA', 'Puebla'), ('QUERETARO', 'Queretaro'), ('QUINTANA ROO', 'Quintana Roo'), ('SAN LUIS POTOSI', 'San Luis Potosi'), ('SINALOA', 'Sinaloa'), ('SONORA', 'Sonora'), ('TABASCO', 'Tabasco'), ('TAMAULIPAS', 'Tamaulipas'), ('TLAXCALA', 'Tlaxcala'), ('VERACRUZ DE IGNACIO DE LA LLAVE', 'Veracruz'), ('YUCATAN', 'Yucatan'), ('ZACATECAS', 'Zacatecas')])),
                ('type_of_person', models.CharField(choices=[('M', 'Persona Moral'), ('F', 'Persona Física')], max_length=1)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='PersonDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rfc', models.CharField(max_length=13)),
                ('social_reason', models.TextField(max_length=250)),
                ('date_published', models.DateField()),
                ('type_of_person', models.CharField(choices=[('M', 'Persona Moral'), ('F', 'Persona Física')], max_length=1)),
                ('state', models.CharField(verbose_name=[('AGUASCALIENTES', 'Aguascalientes'), ('BAJA CALIFORNIA', 'Baja California'), ('BAJA CALIFORNIA SUR', 'Baja California Sur'), ('CAMPECHE', 'Campeche'), ('CHIAPAS', 'Chiapas'), ('CHIHUAHUA', 'Chihuahua'), ('CIUDAD DE MEXICO', 'Ciudad De Mexico'), ('COAHUILA DE ZARAGOZA', 'Coahuila'), ('COLIMA', 'Colima'), ('DURANGO', 'Durango'), ('GUANAJUATO', 'Guanajuato'), ('GUERRERO', 'Guerrero'), ('HIDALGO', 'Hidalgo'), ('JALISCO', 'Jalisco'), ('MEXICO', 'Estado de México'), ('MICHOACAN DE OCAMPO', 'Michoacán'), ('MORELOS', 'Morelos'), ('NAYARIT', 'Nayarit'), ('NUEVO LEON', 'Nuevo Leon'), ('OAXACA', 'Oaxaca'), ('PUEBLA', 'Puebla'), ('QUERETARO', 'Queretaro'), ('QUINTANA ROO', 'Quintana Roo'), ('SAN LUIS POTOSI', 'San Luis Potosi'), ('SINALOA', 'Sinaloa'), ('SONORA', 'Sonora'), ('TABASCO', 'Tabasco'), ('TAMAULIPAS', 'Tamaulipas'), ('TLAXCALA', 'Tlaxcala'), ('VERACRUZ DE IGNACIO DE LA LLAVE', 'Veracruz'), ('YUCATAN', 'Yucatan'), ('ZACATECAS', 'Zacatecas')])),
                ('assumption', models.CharField(choices=[('FIRME', 'Firme'), ('EXIGIBLE', 'Exigible'), ('NO LOCALIZADO', 'No Localizado')], max_length=13)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
