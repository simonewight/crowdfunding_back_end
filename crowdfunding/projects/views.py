from rest_framework import generics, permissions
from rest_framework.response import Response
from django.db.models import Prefetch, Sum, Count
from .models import Project, Pledge
from .serializers import ProjectSerializer, PledgeSerializer, ProjectDetailSerializer
from .permissions import IsOwnerOrReadOnly

class ProjectList(generics.ListCreateAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Project.objects.annotate(
            total_pledges=Sum('project_pledges__amount'),
            pledges_count=Count('project_pledges')
        ).prefetch_related(
            Prefetch(
                'project_pledges',
                queryset=Pledge.objects.select_related('supporter')
            )
        ).order_by('-date_created')

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]

    def get_queryset(self):
        return Project.objects.annotate(
            total_pledges=Sum('project_pledges__amount'),
            pledges_count=Count('project_pledges')
        ).prefetch_related(
            Prefetch(
                'project_pledges',
                queryset=Pledge.objects.select_related('supporter')
            )
        )

    serializer_class = ProjectDetailSerializer

class PledgeList(generics.ListCreateAPIView):
    queryset = Pledge.objects.all()
    serializer_class = PledgeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(supporter=self.request.user)

class PledgeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pledge.objects.all()
    serializer_class = PledgeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ProjectPledgeList(generics.ListAPIView):
    serializer_class = PledgeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Pledge.objects.filter(project_id=self.kwargs.get('pk'))