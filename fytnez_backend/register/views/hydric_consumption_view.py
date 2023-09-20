from rest_framework import viewsets

from fytnez_backend.register.models.hydric_consumption import HydricConsumption
from fytnez_backend.register.serializers.hydric_consumption_serializer import HydricConsumptionSerializer



class HydricConsumptionView(viewsets.ModelViewSet):
    queryset = HydricConsumption.objects.filter(delete_at__isnull=True)
    serializer_class = HydricConsumptionSerializer
