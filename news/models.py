from django.db import models


# Create your models here.
class Articles(models.Model):
    title = models.CharField('Назва', max_length=50, default='')
    anons = models.CharField('Анонс', max_length=250, default='')
    full_text = models.TextField('Стаття')
    date = models.DateTimeField('Publication date')

    def __str__(self):
        return self.title
        # return f"News: {self.title}"

    def get_absolute_url(self):
        return f"/news/{self.id}"

    class Meta:
        verbose_name = "Новину"
        verbose_name_plural = "Новини"
