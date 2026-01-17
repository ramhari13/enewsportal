from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Define the Category model to categorize articles
class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category_images/', blank=True, null=True)


    def __str__(self):
        return self.name

# Define the Article model with fields for title, content, image, video, and category
# video_url , external_link. created_at, updated_at
#ForeignKey Category, User
class Article(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True, blank=True)
    content = models.TextField()
    image = models.ImageField(upload_to='articles/', blank=True, null=True)
    video = models.FileField(upload_to='articles/videos/', blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    external_link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='articles')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    is_breaking_news = models.BooleanField(default=False)

    def __str__(self):
        return self.title



# Profile model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

'''# Signal to create or update the profile when the user is created or updated
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    # Always save the profile when the user is saved
    instance.profile.save()
'''


#comment

class Comment(models.Model):
    article = models.ForeignKey('Article', on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # This links the comment to a user
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.name} on {self.article.title}'
    


"""
# models.py
from django.db import models
from django.contrib.auth.models import User
import uuid

class Comment(models.Model):
    article = models.ForeignKey('Article', on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # Links the comment to a user (optional)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, null=True, blank=True)  # Token for anonymous users

    def __str__(self):
        return f'Comment by {self.name} on {self.article.title}'"""
