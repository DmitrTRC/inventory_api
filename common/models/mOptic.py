from django.db import models


class Optic(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='optics_item_photos', blank=True)
    optics_type = models.CharField(max_length=100, blank=False, null=False, default='Day')

    def __str__(self):
        return self.name
