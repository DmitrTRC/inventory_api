from django.contrib import admin

from common.models.mLicense import License
from common.models.mOptic import Optic
from common.models.mWeapon import WeaponItem

admin.site.register(WeaponItem)
admin.site.register(License)
admin.site.register(Optic)

