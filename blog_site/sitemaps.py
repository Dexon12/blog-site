from django.contrib.sitemaps import Sitemap
from .models import Post

class PostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9
    
    def items(self):
        return Post.published.all()
    
    def lastmod(self, obj): # Как джанго понимает как с ними взаимодействовать? Эти методы встроенные и мы их просто переопределяем?
        return obj.updated