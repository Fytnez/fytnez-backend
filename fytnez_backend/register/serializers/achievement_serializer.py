from rest_framework import serializers

from fytnez_backend.register.models.achievement import Achievement


class AchievementSerializer(serializers.HyperlinkedModelSerializer):
    type = serializers.SerializerMethodField()
    icon = serializers.SerializerMethodField()
    
    class Meta:
        model = Achievement
        fields = '__all__'
        
    def get_type(self, instance: Achievement):
        return instance.type.name
    
    def get_icon(self, instance: Achievement):
        return instance.type.icon