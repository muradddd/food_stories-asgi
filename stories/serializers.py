from rest_framework import serializers
from accounts.models import (User,)
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'bio')


class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = ('title', 'description', 'category', 'tag', )

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name',)