from rest_framework import generics, permissions
from rest_framework.response import Response
from django.db.models import Prefetch, Sum, Count, F
from .models import Project, Pledge
from .serializers import ProjectSerializer, PledgeSerializer, ProjectDetailSerializer
from .permissions import IsOwnerOrReadOnly

class ProjectList(generics.ListCreateAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Project.objects.annotate(
            total_pledges=Sum('project_pledges__amount', default=0),
            pledges_count=Count('project_pledges', distinct=True)
        ).prefetch_related(
            Prefetch(
                'project_pledges',
                queryset=Pledge.objects.select_related('supporter')
            )
        ).order_by('-date_created')

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['include_pledges'] = True
        return context

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        print("Response data:", response.data)
        return response

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectDetailSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
        return response

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