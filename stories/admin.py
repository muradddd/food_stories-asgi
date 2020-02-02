from django.contrib import admin
from .models import *



# class AppendInline(admin.TabularInline):
#     model = Append

@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ['title', ]



@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active']
    list_filter = ('is_active', )
    search_fields = ('name', )
    actions = ['make_tags_active', 'make_tags_inactive']

    def make_tags_active(self, request, queryset):
        queryset.update(is_active=True)
    make_tags_active.short_description = "Mark selected tags as active"

    def make_tags_inactive(self, request, queryset):
        queryset.update(is_active=False)
    make_tags_inactive.short_description = "Mark selected tags as inactive"


admin.site.register(Recipe)
# admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Subscribe)
# admin.site.register(Tag)
admin.site.register(Contact)
