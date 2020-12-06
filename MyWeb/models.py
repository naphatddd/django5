from django.db import models

# Create your models here.
class tb_news3(models.Model):
    news_title = models.CharField(max_length=300)
    news_detail = models.TextField()
    news_center = models.CharField(max_length=300)
    news_photo = models.ImageField(upload_to='Photo', default='')
    news_date = models.DateTimeField(auto_now=True, blank=False)