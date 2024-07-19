from django.contrib import admin
from rest_framework.exceptions import ValidationError
from django import forms
from .models import UserForm1, UserForm2, Images, Videos, News, CategoryNews, TrendingStories, SpeechAnalysis


class ImagesInline(admin.TabularInline):
    model = News.images.through
    extra = 1


class VideosInline(admin.StackedInline):
    model = News.videos.through
    extra = 1


class NewsAdmin(admin.ModelAdmin):
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


class UserForm1Admin(admin.ModelAdmin):
    form = UserForm1AdminForm
    list_display = ('full_name', 'phone', 'email', 'nationality', 'date', 'amount')
    search_fields = ('full_name', 'nationality')
    readonly_fields = ('email',)


class UserForm2Admin(admin.ModelAdmin):
    list_display = ('full_name', 'role', 'email')
    search_fields = ('full_name', 'role')


class ImagesAdmin(admin.ModelAdmin):
    list_display = ('sub_title1', 'sub_description1', 'sub_title2', 'sub_description2')
    search_fields = ('sub_title1',)


class VideosAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title',)


class CategoryNewsAdmin(admin.ModelAdmin):
    list_display = ('title1', 'title2', 'created_at')
    search_fields = ('title1', 'title2')


class TrendingStoriesAdmin(admin.ModelAdmin):
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
