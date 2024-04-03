from rest_framework import serializers
from baseusermaster.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'status_toggle'] 
        extra_kwargs = {'password': {'write_only': True}}

