from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.urls import reverse

# class Author(models.Model):
#     authorUser = models.OneToOneField(User, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return '{}'.format(self.authorUser)
#
# class Category(models.Model):
#     name = models.CharField(max_length=64, unique=True)
#     subscribers = models.ManyToManyField(User, blank=True)
#
#     def __str__(self):
#         return self.name.title()
#
#     class Meta:
#         verbose_name = 'Category'
#         verbose_name_plural = 'Categories'

class Post(models.Model):
    TYPE = [
        ('tank', 'Танки'),
        ('heal', 'Хилы'),
        ('dd', 'ДД'),
        ('buyers', 'Торговцы'),
        ('guildmaster', 'Гилдмастеры'),
        ('quest', 'Квестгиверы'),
        ('smith', 'Кузнецы'),
        ('tanner', 'Кожевники'),
        ('potion', 'Зельевары'),
        ('spellmaster', 'Мастера заклинаний')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    text = models.TextField()
    category = models.CharField(max_length=64, choices=TYPE, default='tank')
    # postCategory = models.ManyToManyField(Category, through='PostCategory')
    dateCreation = models.DateField(auto_now=True)
    # upload = models.FileField(upload_to='uploads/')

    def preview(self):
        return self.text[0:123] + '...'

    def __str__(self):
        return f'{self.title}: {self.text[:20]}, {self.category} '

    def get_absolute_url(self):
        return reverse('board')

# class PostCategory(models.Model):
#     postThrough = models.ForeignKey(Post, on_delete=models.CASCADE)
#     categoryThrough = models.ForeignKey(Category, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return '{}'.format(self.categoryThrough)
#
#     class Meta:
#         verbose_name = 'Post category'
#         verbose_name_plural = 'Post categories'
#
# class Comment(models.Model):
#     commentPost = models.ForeignKey(Post, on_delete=models.CASCADE)
#     commentUser = models.ForeignKey(User, on_delete=models.CASCADE)
#     text = models.TextField()
#     dateCreation = models.DateField(auto_now_add=True)

class UserResponse(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    article = models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    creation = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-creation']

    def __str__(self):
        return f'{self.author}. {self.creation}: {self.text}'

class OneTimeCode(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=10)
    creation = models.DateTimeField(auto_now_add=True)

class MassMail(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} - {self.creation}'
