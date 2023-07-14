from django.db import models

from common.models.mCaliber import Caliber


class WeaponItem(models.Model):
    item_model = models.ForeignKey('WeaponModel', on_delete=models.RESTRICT, blank=False, null=False)
    item_license = models.ForeignKey('License', on_delete=models.RESTRICT, blank=False, null=True)
    description = models.CharField(max_length=200)
    barrel_number = models.IntegerField(default=0)
    barrel_shots = models.IntegerField(default=0)
    is_cleared = models.BooleanField(default=False)
    is_need_repair = models.BooleanField(default=False)
    last_clean = models.DateField(blank=True, null=True)
    last_shoot = models.DateField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.item_model.name


# TODO: Refactor to lazy load
class WeaponModel(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='weapon_item_photos', blank=True)
    caliber = models.ForeignKey(Caliber, on_delete=models.RESTRICT, blank=False, null=True)
    manufacturer = models.ForeignKey('WeaponManufacturer', on_delete=models.RESTRICT, blank=False, null=True)

    def __str__(self):
        return self.name


class WeaponManufacturer(models.Model):
    brand_name = models.CharField(max_length=200)
    country = models.CharField(max_length=100, blank=False, null=False, default='USA')
    website = models.CharField(max_length=100, blank=False, null=False, default='https://www.google.com')

    def __str__(self):
        return self.name
