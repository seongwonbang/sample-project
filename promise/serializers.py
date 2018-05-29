from django.db.models import Q

from rest_framework import serializers

from .models import *


class PromiseSerializer(serializers.ModelSerializer):
    user1 = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Promise
        fields = '__all__'


class UserPromiseSerializer(serializers.ModelSerializer):
    user1 = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    user2 = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    def to_representation(self, obj):
        whole_promises = obj.user1.all() | obj.user2.all()
        return {
            'id': obj.id,
            'username': obj.username,
            'whole_promises': whole_promises.values_list('id', flat=True)
        }

    class Meta:
        model = User
        fields = ('id', 'username', 'user1', 'user2')
