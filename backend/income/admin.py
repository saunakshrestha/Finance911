from django.contrib import admin
from income.models import Income
# Register your models here.


class IncomeAdmin(admin.ModelAdmin):
    list_display = ['id', 'amount', 'source', 'date', 'description','user']
    search_fields = ['source', 'description']
    list_filter = ['source', 'date']
    list_per_page = 10

admin.site.register(Income, IncomeAdmin)
