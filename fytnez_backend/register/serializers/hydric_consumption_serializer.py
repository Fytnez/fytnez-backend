from rest_framework import serializers

from fytnez_backend.register.models.hydric_consumption import HydricConsumption


class HydricConsumption(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HydricConsumption
        fields = '__all__'