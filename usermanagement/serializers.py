from rest_framework import serializers
from .models import TempUserMaster

class TempUserMasters(serializers.ModelSerializer):
    

    class Meta:
        model = TempUserMaster
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return {
            'id': representation['id'],
            'username': representation['username'],
            'email': representation['email'],
            'status_toggle': representation['status_toggle'],
        }
