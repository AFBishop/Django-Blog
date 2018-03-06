from django.contrib import admin

from Bolg.models import Django, Python, Category

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    pass


class DjangoAdmin(admin.ModelAdmin):
    pass


class PythonAdmin(admin.ModelAdmin):
    pass


admin.site.register(Category, CategoryAdmin)
admin.site.register(Django, DjangoAdmin)
admin.site.register(Python, PythonAdmin)
