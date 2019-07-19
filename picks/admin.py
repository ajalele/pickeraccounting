from django.contrib import admin
from picks.models import Pick


class PickAdmin(admin.ModelAdmin):
	list_display = ('item', 'date_bought')

admin.site.register(Pick, PickAdmin)