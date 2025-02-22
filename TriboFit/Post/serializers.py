from rest_framework import serializers
from .models import Post, Tag
from User.models import TheUser
from User.functions_auxiliaries import Procurar_User

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'description', 'creator', 'post', 'tags']
        extra_kwargs = {'creator': {'read_only': True}}
    
    def create(self, validated_data):
        request = self.context['request']
        tags = validated_data.pop('tags', [])
        validated_data['creator'] = Procurar_User(request)

        post = Post.objects.create(**validated_data)
        post.save()

        for tag_name in tags:
            tag, _ = Tag.objects.get_or_create(tag_name)
            post.tags.add(tag)

        return post
