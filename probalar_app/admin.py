from django.contrib import admin
from django.contrib.auth.models import Group, User

from import_export.admin import ImportExportModelAdmin
from .models import Aprel_1, Aprel_2, Dekabr_1, Dekabr_2, Fevral_1, Fevral_2, Mart_1, Mart_2, May_1, May_2, Noyabr_1, Noyabr_2, Oktyabr_1, Oktyabr_2, Sentyabr_1, Sentyabr_2, Yanvar_1, Yanvar_2


# Register your models here.
admin.site.unregister(Group)
admin.site.unregister(User)


@admin.register(Sentyabr_1)
@admin.register(Oktyabr_1)
@admin.register(Noyabr_1)
@admin.register(Dekabr_1)
@admin.register(Yanvar_1)
@admin.register(Fevral_1)
@admin.register(Mart_1)
@admin.register(Aprel_1)
@admin.register(May_1)
@admin.register(Sentyabr_2)
@admin.register(Oktyabr_2)
@admin.register(Noyabr_2)
@admin.register(Dekabr_2)
@admin.register(Yanvar_2)
@admin.register(Fevral_2)
@admin.register(Mart_2)
@admin.register(Aprel_2)
@admin.register(May_2)

class ViewAdmin(ImportExportModelAdmin):
    pass