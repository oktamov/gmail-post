from django.contrib import admin
from .models import UserForm1, UserForm2, Videos, Images, News


class UserForm1Admin(admin.ModelAdmin):
    list_display = ('full_name', 'phone', 'email', 'nationality', 'date', 'address', 'amount')
    search_fields = ('full_name', 'email', 'nationality')
    list_filter = ('nationality', 'date')
    date_hierarchy = 'date'


class UserForm2Admin(admin.ModelAdmin):
    list_display = ('full_name', 'role', 'email')
    search_fields = ('full_name', 'email')
    list_filter = ('role',)


admin.site.register(UserForm1, UserForm1Admin)
admin.site.register(UserForm2, UserForm2Admin)


class ImagesInline(admin.TabularInline):
    model = News.images.through
    extra = 1
    verbose_name = 'Image'
    verbose_name_plural = 'Related Images'


# Inline admin for Videos inside News
class VideosInline(admin.TabularInline):
    model = News.videos.through
    extra = 1
    verbose_name = 'Video'
    verbose_name_plural = 'Related Videos'


# Admin for News
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    inlines = [ImagesInline, VideosInline]
    list_display = ('title', 'status', 'description_short')
    list_filter = ('status',)
    search_fields = ('title', 'description')
    exclude = ('images', 'videos',)  # Exclude the direct many-to-many fields to use inlines instead

    def description_short(self, obj):
        return (obj.description[:50] + '...') if len(obj.description) > 50 else obj.description

    description_short.short_description = 'Description'


# Optionally, register Images and Videos if not already done
@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    list_display = ['id', 'image']


@admin.register(Videos)
class VideosAdmin(admin.ModelAdmin):
    list_display = ['id', 'video']
