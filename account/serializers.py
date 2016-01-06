from rest_framework.serializers import ModelSerializer
from ember_drf.serializers import SideloadSerializer
from account.models import Message



class MessageSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = ('status', 'to', 'message')


class MessageSideloadSerializer(SideloadSerializer):
    class Meta:
        base_serializer = MessageSerializer
