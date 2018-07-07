from django.contrib import admin
from .models import Article
# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    # 除了元祖,也支持列表,元素为列字段
    list_display = ('id', 'title', 'pub_time')
    # 过滤器
    list_filter = ('pub_time',)
    # 官方文档
    # https: // docs.djangoproject.com / en / 2.0 / ref / contrib / admin /


admin.site.register(Article, ArticleAdmin)
