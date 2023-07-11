from django.db import models


class License(models.Model):
    license_number = models.CharField(max_length=200)
    expiration_date = models.DateField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='license_photos', blank=True)
    is_active = models.BooleanField(default=True)
    weapon_item = models.ForeignKey('WeaponItem', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.license_number
