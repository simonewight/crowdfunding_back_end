from rest_framework import generics, permissions
from rest_framework.response import Response
from django.db.models import Sum, Count
from .models import Project, Pledge
from .serializers import ProjectSerializer, PledgeSerializer, ProjectDetailSerializer
from .permissions import IsOwnerOrReadOnly
import logging

logger = logging.getLogger(__name__)

class ProjectList(generics.ListCreateAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        try:
            # Start with basic query
            queryset = Project.objects.all()
            
            # Log the basic query
            logger.info(f"Basic query count: {queryset.count()}")
            
            # Add annotations
            queryset = queryset.annotate(
                total_pledges=Sum('project_pledges__amount', default=0),
                pledges_count=Count('project_pledges')
            )
            
            # Log after annotations
            logger.info("Added annotations")
            
            # Add related data
            queryset = queryset.prefetch_related('project_pledges')
            
            # Log final query
            logger.info(f"Final query count: {queryset.count()}")
            
            return queryset.order_by('-date_created')
            
        except Exception as e:
            logger.error(f"Error in get_queryset: {str(e)}")
            logger.exception(e)
            raise

    def list(self, request, *args, **kwargs):
        try:
            return super().list(request, *args, **kwargs)
        except Exception as e:
            logger.error(f"Error in list: {str(e)}")
            logger.exception(e)
            raise

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]
    serializer_class = ProjectDetailSerializer

    def get_queryset(self):
        return Project.objects.annotate(
            total_pledges=Sum('project_pledges__amount', default=0),
            pledges_count=Count('project_pledges')
        ).prefetch_related('project_pledges')

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