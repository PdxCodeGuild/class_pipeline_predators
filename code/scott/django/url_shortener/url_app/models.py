from django.db import models

class UrlShortener(models.Model):
    url_name = models.CharField(max_length = 300)
    url_short = models.CharField(max_length = 100)

    def __str__(self):
        return self.url_name
