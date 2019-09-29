from django.contrib import admin
from .models import Story, Region

@admin.register(Story) # decorator 형태로 등록
class StoryAdmin(admin.ModelAdmin):
	list_display = ['title', 'author', 'written_date', 'traveled_start_date', 'traveled_end_date', 'region', 'spot', 'color']
	
@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
	list_display = ['id', 'region', 'base_color']
	


