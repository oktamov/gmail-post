from import_export import resources
from .models import UserForm1, UserForm2, Images, Videos, News, CategoryNews, TrendingStories

class UserForm1Resource(resources.ModelResource):
    class Meta:
        model = UserForm1

class UserForm2Resource(resources.ModelResource):
    class Meta:
        model = UserForm2

class ImagesResource(resources.ModelResource):
    class Meta:
        model = Images

class VideosResource(resources.ModelResource):
    class Meta:
        model = Videos

class NewsResource(resources.ModelResource):
    class Meta:
        model = News

class CategoryNewsResource(resources.ModelResource):
    class Meta:
        model = CategoryNews

class TrendingStoriesResource(resources.ModelResource):
    class Meta:
        model = TrendingStories
