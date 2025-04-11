from django.contrib import admin

# Register your models here.
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'comment', 'created_at')
    search_fields = ('name', 'email')
    list_filter = ('created_at',)
    ordering = ('-created_at',)