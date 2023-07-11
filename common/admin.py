from django.contrib import admin

from common.models.mLicense import License
from common.models.mWeapon import WeaponItem

admin.site.register(WeaponItem)
admin.site.register(License)
