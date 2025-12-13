from django.contrib import admin

from .models import Birthday, Tag

admin.site.empty_value_display = 'Не задано'

class BirthdayAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'birthday',
    )
    list_display_links = ('first_name',)
    list_editable = (
        'last_name',
        'birthday',
    )
    
# Регистрируем класс с настройками админки для моделей IceCream и Category:
admin.site.register(Birthday, BirthdayAdmin)
admin.site.register(Tag)

