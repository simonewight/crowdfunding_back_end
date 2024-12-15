from rest_framework import generics, permissions
from .models import Project, Pledge
from .serializers import ProjectSerializer, PledgeSerializer, ProjectDetailSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.response import Response

class ProjectList(generics.ListCreateAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Project.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    serializer_class = ProjectDetailSerializer
    queryset = Project.objects.all()

class PledgeList(generics.ListCreateAPIView):
    serializer_class = PledgeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Pledge.objects.all()

    def perform_create(self, serializer):
        serializer.save(supporter=self.request.user)

class PledgeDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    serializer_class = PledgeSerializer

    def get_queryset(self):
        return Pledge.objects.all()

class ProjectPledgeList(generics.ListCreateAPIView):
    serializer_class = PledgeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        project_id = self.kwargs['pk']
        return Project.objects.all().order_by('-date_created')  # Add this order_by

    def perform_create(self, serializer):
        project_id = self.kwargs['pk']
        project = Project.objects.get(id=project_id)
        serializer.save(supporter=self.request.user, project=project)