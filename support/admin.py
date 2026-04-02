from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Conversation, Message, CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Extra Fields', {'fields': ('phone_number',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Extra Fields', {'fields': ('phone_number',)}),
    )
    list_display = ['username', 'email', 'phone_number', 'is_staff']


@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'updated_at')
    search_fields = ('id',)

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('conversation', 'sender', 'timestamp', 'get_content_snippet')
    list_filter = ('sender', 'timestamp')
    search_fields = ('content',)

    def get_content_snippet(self, obj):
        return obj.content[:50]
    get_content_snippet.short_description = 'Content'
