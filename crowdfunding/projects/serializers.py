from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Project, Pledge
from datetime import datetime

class DateTimeFieldWithoutTZ(serializers.DateTimeField):
    def to_representation(self, value):
        if value:
            return value.strftime('%Y-%m-%d %H:%M:%S')
        return None

class PledgeSerializer(serializers.ModelSerializer):
    supporter_username = serializers.ReadOnlyField(source='supporter.username')
    date_created = DateTimeFieldWithoutTZ()

    class Meta:
        model = Pledge
        fields = ['id', 'amount', 'comment', 'anonymous', 'project', 'supporter', 'supporter_username', 'date_created']
        read_only_fields = ['id', 'supporter', 'date_created']

class ProjectSerializer(serializers.ModelSerializer):
    owner_username = serializers.ReadOnlyField(source='owner.username')
    pledges = PledgeSerializer(many=True, read_only=True)
    total_pledges = serializers.SerializerMethodField()
    pledges_count = serializers.SerializerMethodField()
    date_created = DateTimeFieldWithoutTZ()

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'goal', 'image', 'is_open', 
                 'date_created', 'date_end', 'owner', 'owner_username', 
                 'pledges', 'category', 'total_pledges', 'pledges_count']
        read_only_fields = ['id', 'owner', 'date_created']

    def get_total_pledges(self, obj):
        return sum(pledge.amount for pledge in obj.pledges.all())

    def get_pledges_count(self, obj):
        return obj.pledges.count()

class ProjectDetailSerializer(ProjectSerializer):
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.goal = validated_data.get('goal', instance.goal)
        instance.image = validated_data.get('image', instance.image)
        instance.is_open = validated_data.get('is_open', instance.is_open)
        instance.date_end = validated_data.get('date_end', instance.date_end)
        instance.category = validated_data.get('category', instance.category)
        instance.save()
        return instance