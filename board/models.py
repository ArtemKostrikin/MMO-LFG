from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name="Название категории")

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    title = models.CharField(max_length=256, verbose_name="Заголовок")
    text = RichTextUploadingField(verbose_name="Содержание поста")
    date_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('post_detail', args=[str(self.id)])


class Response(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Откликнулся")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='responses', verbose_name="Объявление")
    text = models.TextField(verbose_name="Текст отклика")
    status = models.BooleanField(default=False, verbose_name="Статус (Принят/Нет)")
    date_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Отклик от {self.author.username} к "{self.post.title}"'