from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups', 'object_types']

    object_types = serializers.SerializerMethodField(read_only=True, default=[])

    def get_object_types(self, obj):
        return ['<%s: %s>' % (obj.__class__.__name__, obj)]




class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
