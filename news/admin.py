from django.contrib import admin
from .models import Article, Category, Profile, Comment



# Register the Article model in the admin interface

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'video', 'category', 'author', 'is_breaking_news', 'created_at')
    search_fields = ('title', 'content')
    list_filter = ('category', 'is_breaking_news')
    ordering = ('-created_at',)


# Register the Category model in the admin interface
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)  

# Register the Profile model in the admin interface
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'profile_picture')  
    search_fields = ('user__username',)  
    list_filter = ('user',)  

#comment model in the admin
class CommentAdmin(admin.ModelAdmin):
    list_display = ('article', 'name', 'user', 'email', 'created_at')
    search_fields = ('name', 'email', 'message')
    list_filter = ('created_at',)


# Register the All model
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Comment, CommentAdmin)
