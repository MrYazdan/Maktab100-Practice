from .models import Post, Comment, Category
from rest_framework import serializers


# class CommentSerializer(serializers.HyperlinkedModelSerializer):
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'author', 'content', 'replies', 'reply')
        # depth = 2


class PostSerializer(serializers.ModelSerializer):

    def to_internal_value(self, data):
        if (new_category := data.get('category')) and isinstance(new_category, dict):
            new_category = Category.objects.get_or_create(**new_category)
            data['category'] = new_category

        return data

    # comments = serializers.SerializerMethodField()

    # def get_comments(self, obj):
    #     return CommentSerializer(Comment.objects.filter(reply=None), many=True).data

    # def to_representation(self, instance):
    #     print(instance)
    #     instance.name = 'reza'
    #     return "salam"

    class Meta:
        # exclude = ('is_active', )
        fields = ("id", "title", "description", "is_active", "category", "comments")
        # extra_kwargs = {
        #     'comments': {'read_only': True}
        # }
        # extra_fields = 'comments'
        # write_only_fields = ('is_active', )
        model = Post
        depth = 1
