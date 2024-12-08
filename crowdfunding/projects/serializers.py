from rest_framework import serializers
from django.db.models import Sum
from django.contrib.auth import get_user_model
from .models import Project, Pledge

class PledgeSerializer(serializers.ModelSerializer):
    supporter_username = serializers.ReadOnlyField(source='supporter.username')
    
    class Meta:
        model = Pledge
        fields = [
            'id',
            'amount',
            'comment',
            'anonymous',
            'project',
            'supporter',
            'supporter_username',
            'date_created'
        ]
        read_only_fields = ['id', 'supporter', 'date_created']

class ProjectSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')
    owner_username = serializers.ReadOnlyField(source='owner.username')
    total_pledges = serializers.IntegerField(read_only=True, default=0)
    pledges_count = serializers.IntegerField(read_only=True, default=0)
    pledges = PledgeSerializer(many=True, read_only=True, source='project_pledges')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        # Ensure total_pledges is at least 0
        data['total_pledges'] = data.get('total_pledges', 0) or 0
        data['pledges_count'] = data.get('pledges_count', 0) or 0
        return data

    class Meta:
        model = Project
        fields = [
            'id',
            'title',
            'description',
            'goal',
            'image',
            'is_open',
            'date_created',
            'owner',
            'owner_username',
            'total_pledges',
            'pledges_count',
            'pledges'
        ]

class ProjectDetailSerializer(ProjectSerializer):
    class Meta:
        model = Project
        fields = ProjectSerializer.Meta.fields