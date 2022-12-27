from posts.models import Comment, Follow, Group, Post, User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.validators import UniqueTogetherValidator


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description',)


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
    )

    class Meta:
        model = Comment
        fields = ('id', 'author', 'text', 'created', 'post',)
        read_only_fields = ('post',)


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
    )

    class Meta:
        model = Post
        fields = ('id', 'author', 'text', 'pub_date', 'image', 'group',)


class FollowSerializer(serializers.ModelSerializer):
    following = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username',
    )

    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Follow
        fields = ('user', 'following',)
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'following'),
            )
        ]

    def validate_following(self, value):
        if value == self.context['request'].user:
            raise ValidationError('Нельзя подписаться на себя!')
        return value
