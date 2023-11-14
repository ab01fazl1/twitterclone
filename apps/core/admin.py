# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from .models import User,Tweet,Relationship,Like,Hashtag,Retweet
#
#
# class UserAdmin(BaseUserAdmin):
#     fieldsets = (
#         (None, {'fields': ('username', 'password', 'email', 'last_login')}),
#         ('Permissions', {'fields': (
#             'is_active',
#             'is_staff',
#             'is_superuser',
#             'groups',
#             'user_permissions',
#         )}),
#     )
#     add_fieldsets = (
#         (
#             None,
#             {
#                 'classes': ('wide',),
#                 'fields': ('username', 'password1', 'password2')
#             }
#         ),
#     )
#
#     list_display = ('username', 'email', 'is_staff', 'last_login')
#     list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
#     search_fields = ('username',)
#     ordering = ('username',)
#     filter_horizontal = ('groups', 'user_permissions',)
#
#
# class TweetAdmin(admin.ModelAdmin):
#     list_display = ('user','text','created_at','is_reply','is_quote')
#
#
#
#
# admin.site.register(User, UserAdmin)
# admin.site.register(Tweet,TweetAdmin)
# admin.site.register(Relationship)
# admin.site.register(Like)
# admin.site.register(Hashtag)
# admin.site.register(Retweet)
#
#
#
