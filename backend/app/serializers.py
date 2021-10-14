from rest_framework import serializers

from .models import Intern, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "email", "address", "city", "state", "active","staff","admin","date" ]

class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "email", "address", "city", "state"]
        extra_kwargs = { "email": {"required": False} }

class InternSerializer(serializers.Serializer):
    
    name = serializers.CharField(max_length=100)
    stack = serializers.CharField(max_length = 100)
    job = serializers.CharField(max_length=100)
    batch = serializers.IntegerField()

    def create(self, validated_data):
        return Intern.objects.create(**validated_data)
    
    def update(self, instance, validated_data):

        instance.name = validated_data.get('name', instance.name)
        instance.stack = validated_data.get('stack', instance.stack)
        instance.job = validated_data.get('job', instance.job)
        instance.batch = validated_data.get('batch', instance.batch)

        instance.save()
        return instance
