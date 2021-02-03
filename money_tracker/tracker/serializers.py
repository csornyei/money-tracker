from rest_framework import serializers
from tracker.models import Spending

class SpendingSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    amount = serializers.IntegerField()
    currency = serializers.CharField(required=True, max_length=3)
    description = serializers.CharField(required=True, max_length=255)
    date = serializers.DateTimeField()

    def create(self, validated_data):
        return Spending.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.amount = validated_data.get('amount', instance.amount)
        instance.currency = validated_data.get('currency', instance.currency)
        instance.description = validated_data.get('description', instance.description)
        instance.date = validated_data.get('date', instance.date)
        instance.save()
        return instance