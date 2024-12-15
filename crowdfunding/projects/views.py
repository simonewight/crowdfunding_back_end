from rest_framework import generics, permissions
from .models import Project, Pledge
from .serializers import ProjectSerializer, PledgeSerializer, ProjectDetailSerializer
from .permissions import IsOwnerOrReadOnly
from django.http import HttpResponse
from rest_framework.response import Response

class ProjectList(generics.ListCreateAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Project.objects.all()

    def perform_create(self, serializer):
        print("Received data:", self.request.data)  # Debug line
        instance = serializer.save(owner=self.request.user)
        print("Saved project:", instance.date_end)  # Debug line

class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    serializer_class = ProjectDetailSerializer
    queryset = Project.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        print("Project data:", instance.date_end)  # Debug line
        print("Serialized data:", serializer.data)  # Debug line
        return Response(serializer.data)

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
        return Pledge.objects.filter(project_id=project_id)

    def perform_create(self, serializer):
        project_id = self.kwargs['pk']
        project = Project.objects.get(id=project_id)
        serializer.save(supporter=self.request.user, project=project)