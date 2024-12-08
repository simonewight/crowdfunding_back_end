from rest_framework import serializers
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
    total_pledges = serializers.IntegerField(read_only=True)
    pledges_count = serializers.IntegerField(read_only=True)
    pledges = PledgeSerializer(many=True, read_only=True, source='project_pledges')

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