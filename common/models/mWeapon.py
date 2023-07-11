from django.db import models


class WeaponItem(models.Model):
    item_model = models.ForeignKey('ItemModel', on_delete=models.CASCADE)
    item_photo = models.ImageField(upload_to='weapon_item_photos', blank=True)
    item_license = models.ForeignKey('License', on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    caliber = models.FloatField(default=0)
    barrel_number = models.IntegerField(default=0)
    barrel_shots = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    is_cleared = models.BooleanField(default=False)
    is_need_repair = models.BooleanField(default=False)
    is_alligned = models.BooleanField(default=False)
    optics_one = models.ForeignKey('Optic', on_delete=models.CASCADE, related_name='optics_one', blank=True, null=True)
    optics_two = models.ForeignKey('Optic', on_delete=models.CASCADE, related_name='optics_two', blank=True, null=True)
    last_clean = models.DateField(blank=True, null=True)
    last_shoot = models.DateField(blank=True, null=True)
    notes = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.item_model.name


class ItemModel(models.Model):
    name = models.CharField(max_length=200)
    manufacturer = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name
