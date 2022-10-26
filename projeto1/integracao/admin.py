from django.contrib import admin
from integracao.models import Video
# Register your models here.


class Videos(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'descricao', 'url' )
    list_display_links = ('titulo', 'descricao', 'id')
    search_fields = ('titulo',)
    list_per_page = 50

admin.site.register(Video, Videos)