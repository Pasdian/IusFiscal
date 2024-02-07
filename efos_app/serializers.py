from rest_framework import serializers
from .models import Efo, PersonDetail, Cancellation, Art74Reduction

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Efo
        fields = '__all__'


class PersonDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonDetail
        fields = '__all__'


class CancellationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cancellation
        fields = '__all__'
    
    cancel_reason =serializers.SerializerMethodField()

    def get_cancel_reason(self, obj):
        return obj.get_cancel_reason_display()


class ReductionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Art74Reduction
        fields = '__all__'