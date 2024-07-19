from django.contrib import admin
from rest_framework.exceptions import ValidationError
from django import forms
from import_export.admin import ImportExportModelAdmin
from .models import UserForm1, UserForm2, Images, Videos, News, CategoryNews, TrendingStories
from .resources import UserForm1Resource, UserForm2Resource, ImagesResource, VideosResource, NewsResource, CategoryNewsResource, TrendingStoriesResource
from .models import UserForm1, UserForm2, Images, Videos, News, CategoryNews, TrendingStories, SpeechAnalysis


class ImagesInline(admin.TabularInline):
    model = News.images.through
    extra = 1

class VideosInline(admin.StackedInline):
    model = News.videos.through
    extra = 1

class NewsAdmin(ImportExportModelAdmin):
    resource_class = NewsResource
    list_display = ('cover_title', 'title', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('title', 'cover_title')
    inlines = [ImagesInline, VideosInline]
    exclude = ('images', 'videos')

class UserForm1AdminForm(forms.ModelForm):
    class Meta:
        model = UserForm1
        fields = '__all__'

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not phone.startswith('+'):
            raise ValidationError('Telefon raqami "+" belgisi bilan boshlanishi kerak.')
        return phone

class UserForm1Admin(ImportExportModelAdmin):
    resource_class = UserForm1Resource
    form = UserForm1AdminForm
    list_display = ('full_name', 'phone', 'email', 'nationality', 'date', 'amount')
    search_fields = ('full_name', 'nationality')
    readonly_fields = ('email',)

class UserForm2Admin(ImportExportModelAdmin):
    resource_class = UserForm2Resource
    list_display = ('full_name', 'role', 'email')
    search_fields = ('full_name', 'role')

class ImagesAdmin(ImportExportModelAdmin):
    resource_class = ImagesResource
    list_display = ('sub_title1', 'sub_description1', 'sub_title2', 'sub_description2')
    search_fields = ('sub_title1',)

class VideosAdmin(ImportExportModelAdmin):
    resource_class = VideosResource
    list_display = ('title', 'description')
    search_fields = ('title',)

class CategoryNewsAdmin(ImportExportModelAdmin):
    resource_class = CategoryNewsResource
    list_display = ('title1', 'title2', 'created_at')
    search_fields = ('title1', 'title2')

class TrendingStoriesAdmin(ImportExportModelAdmin):
    resource_class = TrendingStoriesResource
    list_display = ('title', 'url')
    search_fields = ('title', 'url')


class SpeechAnalysisAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'company_name', 'email')
    search_fields = ('full_name',)


# Admin ro'yxatga olishlar...
admin.site.register(UserForm1, UserForm1Admin)
admin.site.register(UserForm2, UserForm2Admin)
admin.site.register(Images, ImagesAdmin)
admin.site.register(Videos, VideosAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(CategoryNews, CategoryNewsAdmin)
admin.site.register(TrendingStories, TrendingStoriesAdmin)
admin.site.register(SpeechAnalysis, SpeechAnalysisAdmin)
