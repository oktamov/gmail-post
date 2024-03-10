from rest_framework import serializers
from .models import UserForm1, UserForm2, CategoryNews, Images, Videos, News


class UserForm1Serializer(serializers.ModelSerializer):
    class Meta:
        model = UserForm1
        fields = '__all__'


class UserForm2Serializer(serializers.ModelSerializer):
    class Meta:
        model = UserForm2
        fields = '__all__'


class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField()
    text = serializers.CharField()


class CategoryNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryNews
        fields = ('title1', 'title2', 'url', 'image')


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ('image', 'title', 'description')


class VideosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Videos
        fields = ('video', 'title', 'description')


class NewsSerializer(serializers.ModelSerializer):
    images = ImagesSerializer(many=True, read_only=True)
    videos = VideosSerializer(many=True, read_only=True)

    class Meta:
        model = News
        fields = ('title', 'images', 'videos', 'description', 'status')
