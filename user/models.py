from django.db import models


class UserForm1(models.Model):
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    nationality = models.CharField(max_length=50)
    date = models.DateField()
    address = models.TextField()
    amount = models.IntegerField()

    def __str__(self):
        return self.full_name


class UserForm2(models.Model):
    full_name = models.CharField(max_length=100)
    role = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.full_name


class Images(models.Model):
    image = models.ImageField(upload_to='images')
    sub_title1 = models.CharField(max_length=255)
    sub_description1 = models.TextField()
    sub_title2 = models.CharField(max_length=255, null=True, blank=True)
    sub_description2 = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.sub_title1


class Videos(models.Model):
    video = models.FileField(upload_to='videos')
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title


class News(models.Model):
    STATUS_CHOICES = (
        ('trending', 'Trending stories'),
        ('videos', 'Videos'),
    )

    cover_title = models.CharField(max_length=255)
    cover_image = models.ImageField(upload_to='images', null=True, blank=True)
    title = models.CharField(max_length=255)
    images = models.ManyToManyField(Images, blank=True, related_name='image_news')
    videos = models.ManyToManyField(Videos, blank=True, related_name='video_news')
    description = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='trending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cover_title


class CategoryNews(models.Model):
    title1 = models.CharField(max_length=255)
    title2 = models.CharField(max_length=255, blank=True, null=True)
    url = models.URLField(blank=True)
    image = models.ImageField(upload_to='images')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title1


class TrendingStories(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.title


class SpeechAnalysis(models.Model):
    full_name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.full_name
