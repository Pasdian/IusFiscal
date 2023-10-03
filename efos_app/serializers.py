from rest_framework import serializers
from .models import Efo, PersonDetail

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Efo
        fields = '__all__'


class PersonDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonDetail
        fields = '__all__'