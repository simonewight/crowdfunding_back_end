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
    total_pledges = serializers.SerializerMethodField()
    pledges_count = serializers.SerializerMethodField()
    pledges = PledgeSerializer(many=True, read_only=True, source='project_pledges')
    
    def get_total_pledges(self, obj):
        return obj.get_total_pledges()

    def get_pledges_count(self, obj):
        return obj.get_pledges_count()

    def create(self, validated_data):
        print("Creating project with data:", validated_data)  # Debug line
        instance = super().create(validated_data)
        print("Created project with date_end:", instance.date_end)  # Debug line
        return instance

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
            'date_end',
            'owner',
            'owner_username',
            'total_pledges',
            'pledges_count',
            'pledges',
            'category'
        ]
        read_only_fields = ['id', 'date_created', 'owner']

class ProjectDetailSerializer(ProjectSerializer):
    class Meta:
        model = Project
        fields = ProjectSerializer.Meta.fields  # Remove the + ['date_end'] since it's already in ProjectSerializer