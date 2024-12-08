from rest_framework import serializers
from .models import Project, Pledge
import logging

logger = logging.getLogger(__name__)

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

    def to_representation(self, instance):
        try:
            data = super().to_representation(instance)
            logger.info(f"Serialized project {instance.id}: {data}")
            return data
        except Exception as e:
            logger.error(f"Error serializing project {instance.id}: {str(e)}")
            raise

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
            'owner_username'
        ]

class ProjectDetailSerializer(ProjectSerializer):
    pledges = PledgeSerializer(many=True, read_only=True, source='project_pledges')

    class Meta:
        model = Project
        fields = ProjectSerializer.Meta.fields + ['pledges']