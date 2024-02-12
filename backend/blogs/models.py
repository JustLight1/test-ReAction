from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='blogs')
    title = models.CharField('Название', max_length=100)
    text = models.TextField('Текст')
    created = models.DateTimeField('Дата создания', auto_now_add=True)
    published = models.BooleanField(
        'Опубликовано',
        default=False,
        help_text='Отметьте, чтобы опубликовать запись'
    )

    class Meta:
        ordering = ['created']
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.title
