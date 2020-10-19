import os
from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='Название'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('id', 'name')


class Article(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='Название',
        db_index=True
    )
    content = models.TextField(
        verbose_name='Содержание'
    )
    published = models.DateTimeField(
        verbose_name='Время публикации',
        auto_now_add=True,
        null=True
    )
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.PROTECT)

    def __str__(self):
        return '[{}] {}'.format(self.category, self.name)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ('-published', 'name')


class ArticleImage(models.Model):
    image = models.ImageField(
        verbose_name='Изображение'
    )
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    class Meta:
        db_table = 'management_article_image'
        verbose_name = 'Изображение статьи'
        verbose_name_plural = 'Изображения статей'

    def delete(self):
        os.remove(self.image.path)
        super().delete()
