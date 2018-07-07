from django.db import models

# Create your models here.
# 字段属性 https://docs.djangoproject.com/en/2.0/ref/models/fields/


class Article(models.Model):
    title = models.CharField(max_length=64, default='Title')
    content = models.TextField(null=True)
    pub_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
