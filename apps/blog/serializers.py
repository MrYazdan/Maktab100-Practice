from .models import Post
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        # exclude = ('is_active', )
        fields = '__all__'
        read_only_fields = ('id',)
        write_only_fields = ('is_active', )
        model = Post
