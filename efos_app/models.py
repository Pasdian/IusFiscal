from django.db import models
from django.utils.translation import gettext_lazy as _


class MexicanStates(models.TextChoices):
    AGUASCALIENTES = 'AGUASCALIENTES'
    BAJA_CALIFORNIA = 'BAJA CALIFORNIA'
    BAJA_CALIFORNIA_SUR = 'BAJA CALIFORNIA SUR'
    CAMPECHE = 'CAMPECHE'
    CHIAPAS = 'CHIAPAS'
    CHIHUAHUA = 'CHIHUAHUA'
    CIUDAD_DE_MEXICO = 'CIUDAD DE MEXICO'
    COAHUILA = 'COAHUILA DE ZARAGOZA'
    COLIMA = 'COLIMA'
    DURANGO = 'DURANGO'
    GUANAJUATO = 'GUANAJUATO'
    GUERRERO = 'GUERRERO'
    HIDALGO = 'HIDALGO'
    JALISCO = 'JALISCO'
    ESTADO_DE_MEXICO = 'MEXICO', _('Estado de México')
    MICHOACAN = 'MICHOACAN DE OCAMPO', _('Michoacán')
    MORELOS = 'MORELOS'
    NAYARIT = 'NAYARIT'
    NUEVO_LEON = 'NUEVO LEON'
    OAXACA = 'OAXACA'
    PUEBLA = 'PUEBLA'
    QUERETARO = 'QUERETARO'
    QUINTANA_ROO = 'QUINTANA ROO'
    SAN_LUIS_POTOSI = 'SAN LUIS POTOSI'
    SINALOA = 'SINALOA'
    SONORA = 'SONORA'
    TABASCO = 'TABASCO'
    TAMAULIPAS = 'TAMAULIPAS'
    TLAXCALA = 'TLAXCALA'
    VERACRUZ = 'VERACRUZ DE IGNACIO DE LA LLAVE'
    YUCATAN = 'YUCATAN'
    ZACATECAS = 'ZACATECAS'


class Efo(models.Model):
    DEFINITIVO = 'DEF'
    DESVIRTUADO = 'DES'
    PRESUNTO = 'PRE'
    SENTENCIA_FAVORABLE = 'SFA'
    FISCAL_SITUATION_CHOICES = [
        (DEFINITIVO, 'Definitivo'),
        (DESVIRTUADO, 'Desvirtuado'),
        (PRESUNTO, 'Presunto'),
        (SENTENCIA_FAVORABLE, 'Sentencia_Favorable'),
    ]

    MORAL = 'M'
    PHYSICAL = 'F'
    TYPE_OF_PERSON_CHOICES = [
        (MORAL, 'Persona Moral'),
        (PHYSICAL, 'Persona Física'),
    ]

    rfc = models.CharField(max_length=13, null = False)
    social_reason = models.TextField(max_length=250)
    fiscal_situation = models.CharField(
        max_length=3, choices=FISCAL_SITUATION_CHOICES)
    # Dates
    sat_presumtion_date = models.DateField(null=True)
    dof_presumtion_date = models.DateField(null=True)
    sat_definitive_date = models.DateField(null=True)
    dof_definitive_date = models.DateField(null=True)
    sat_distorted_date = models.DateField(null=True)
    dof_distorted_date = models.DateField(null=True)
    sat_favorable_ruling_date = models.DateField(null=True)
    dof_favorable_ruling_date = models.DateField(null=True)
    # Aditional Info
    sat_presumtion_file_no = models.CharField(blank=True)
    dof_presumtion_file_no = models.CharField(blank=True)
    sat_definitive_file_no = models.CharField(blank=True)
    dof_definitive_file_no = models.CharField(blank=True)
    sat_distorted_file_no = models.CharField(blank=True)
    dof_distorted_file_no = models.CharField(blank=True)
    sat_favorable_ruling_file_no = models.CharField(blank=True)
    dof_favorable_ruling_file_no = models.CharField(blank=True)
    # Additional Info Date
    sat_presumtion_file_date = models.DateField(null=True)
    dof_presumtion_file_date = models.DateField(null=True)
    sat_definitive_file_date = models.DateField(null=True)
    dof_definitive_file_date = models.DateField(null=True)
    sat_distorted_file_date = models.DateField(null=True)
    dof_distorted_file_date = models.DateField(null=True)
    sat_favorable_ruling_file_date = models.DateField(null=True)
    dof_favorable_ruling_file_date = models.DateField(null=True)
    
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.rfc} - {self.social_reason}"


class PersonDetail(models.Model):

    MORAL = 'M'
    PHYSICAL = 'F'
    TYPE_OF_PERSON_CHOICES = [
        (MORAL, 'Persona Moral'),
        (PHYSICAL, 'Persona Física'),
    ]

    FIRME = 'FIRMES'
    EXIGIBLE = 'EXIGIBLES'
    NO_LOCALIZADO = 'NO LOCALIZADOS'
    ASSUMPTION_CHOICES = [
        (FIRME, 'Firme'),
        (EXIGIBLE, 'Exigible'),
        (NO_LOCALIZADO, 'No Localizado')
    ]

    rfc = models.CharField(max_length=13)
    social_reason = models.TextField(max_length=250)
    date_published = models.DateField(null=True)
    type_of_person = models.CharField(blank=True,
                                      max_length=1, choices=TYPE_OF_PERSON_CHOICES)
    state = models.CharField(MexicanStates.choices, blank=True)
    assumption = models.CharField(
        blank=True, max_length=14, choices=ASSUMPTION_CHOICES)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.rfc} - {self.social_reason}"
