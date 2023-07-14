from django.db import models


class Amo(models.Model):
    type = models.ForeignKey('AmoType', on_delete=models.RESTRICT, blank=False, null=True)
    quantity = models.IntegerField(blank=True, null=True, default=0)


class AmoType(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='amo_manufacture_photos', blank=True)
    country = models.CharField(max_length=100, blank=False, null=False, default='USA')
    caliber = models.ForeignKey('Caliber', on_delete=models.RESTRICT, blank=False, null=True, related_name='calibers')
    bullet_weight = models.CharField(max_length=100, blank=False, null=False, default='55gr')
    bullet_type = models.CharField(max_length=100, blank=False, null=False, default='FMJ')
    ballistics_sheet = models.FileField(upload_to='ballistics_sheets', blank=True)
    optimum_distance = models.IntegerField(blank=True, null=True, default=100)
    manufacturer = models.ForeignKey('AmoManufacturer', on_delete=models.CASCADE, blank=False, null=True,
                                     related_name='manufacturers')

    def __str__(self):
        return self.name

    class AmoManufacturer(models.Model):
        name = models.CharField(max_length=100)
        country = models.CharField(max_length=100, blank=False, null=False, default='USA')
        website = models.CharField(max_length=100, blank=False, null=False, default='https://www.google.com')

        def __str__(self):
            return self.name
