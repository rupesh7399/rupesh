from rest_framework import serializers
from .models import User
# from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all())
    class Meta:
        model = User
        fields = ('url','email')