"""
URL configuration for Enewsportal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from news import views
from django.conf.urls.static import static
from django.conf import settings    


from news.views import (
    CustomPasswordResetView,
    CustomPasswordResetDoneView,
    CustomPasswordResetConfirmView,
    CustomPasswordResetCompleteView,
)

urlpatterns = [
     path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('articles/', views.all_articles, name='all_articles'),
    path('delete/<int:id>/', views.delete_article, name='delete_article'), 
    path('create_article/', views.create_article, name='create_article'),
    path('article/<int:id>/', views.article_detail, name='article_detail'),  

    path('articles/category/<str:category_name>/', views.category_articles, name='category_articles'),

    path('update_article/<int:id>/',views.update_article,name='update_article'),
   
    #-----------
    path('profile/', views.profile_view, name='profile'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('update_profile/', views.update_profile, name='update_profile'),

    path('comment/delete/<int:comment_id>/', views.delete_comment, name='delete_comment'),  # Delete comment




 


    
    # Custom Password reset views
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),








]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 
  

admin.site.index_title = "E-NewsPortal"
admin.site.site_header = "E-NewsPortal Admin"
admin.site.site_title = "E-NewsPortal Admin Portal"