from rest_framework.serializers import ModelSerializer

from team.models import Team


class TeamSerializer(ModelSerializer):
    class Meta:
        model = Team
        fields = ["first_name", "last_name", "designation"]
