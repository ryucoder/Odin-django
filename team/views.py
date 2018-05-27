from rest_framework.generics import (CreateAPIView, ListAPIView,
                                     RetrieveAPIView, UpdateAPIView, DestroyAPIView)
from team.models import Team
from team.serializers import TeamSerializer


class TeamCreateView(CreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class TeamListView(ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class TeamDetailView(RetrieveAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class TeamUpdateView(UpdateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class TeamDeleteView(DestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
