from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from .form import UserRegistrationForm, ArticleForm, UserUpdateForm, ProfileUpdateForm, CommentForm
from .models import Article, Category, Profile, Comment
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest
from datetime import datetime

from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django.contrib import messages





# Home page view
def home(request):
    breaking_news = Article.objects.filter(is_breaking_news=True).order_by('-created_at')[:5]  
    top_headlines = Article.objects.all().order_by('-created_at')[:10]  
    categories = Category.objects.all()  

    context = {
        'breaking_news': breaking_news,
        'top_headlines': top_headlines,
        'categories': categories,
    }
    return render(request, 'home.html', context)



#all articles view
def all_articles(request):
    articles = Article.objects.all().order_by('-created_at')  
    return render(request, 'all_articles.html', {'all_articles': articles})



# Registration view
def register(request):

    if request.user.is_authenticated:
        return redirect('home') 
    
    if request.method == 'GET':
        return render(request,'register.html')
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})


# Login view
def login_view(request):

    if request.user.is_authenticated:
        return redirect('home') 

    if request.method == 'GET':
        return render(request,'login.html')
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')
        else:
            return render(request, 'login.html', {'form': form, 'error': 'Invalid username or password'})

    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# Logout view
def logout_view(request):
    logout(request)
    return redirect('login')



# Create article view
@login_required
def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('home')
    else:
        form = ArticleForm()
    return render(request, 'create_article.html', {'form': form})


#delete articles
@login_required
def delete_article(request, id):
    article = get_object_or_404(Article, id=id)

    if request.method == 'POST':
        article.delete()  
        return redirect('dashboard')  

    return render(request, 'delete_article.html', {'article': article})  



#-------------update article

@login_required(login_url='login')
def update_article(request, id):
    article = get_object_or_404(Article, id=id)

    if article.author != request.user:
        return HttpResponseBadRequest('You cannot access this page <a href="/"> Click here </a> to go homepage!')
    form = ArticleForm(instance=article)

    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES,instance=article)
        if form.is_valid():
            article = form.save(commit=False)
            article.updated_at = datetime.now()
            article.save()
            return redirect('all_articles')  
        else:
            context = {'form': form, 'error': 'Invalid form submission, try again!'}
            return render(request, 'update_article.html', context)  
    context = {'form': form}
    return render(request, 'update_article.html', context)


#-------------


'''
new
#articles details
def article_detail(request, id):
    article = get_object_or_404(Article, id=id)
    return render(request, 'article_detail.html', {'article': article})
'''


def category_articles(request, category_name):
    try:
        category = Category.objects.get(name=category_name)
        articles = Article.objects.filter(category=category).order_by('-created_at')
        return render(request, 'category_articles.html', {'articles': articles, 'category': category})
    
    except Category.DoesNotExist:
        return HttpResponseBadRequest(f'Category "{category_name}" does not exist. <a href="/">Click here</a> to go to the homepage!')


# Profile view
@login_required
def profile_view(request):
    user = request.user
    return render(request, 'user_profile.html', {'user': user})

# Dashboard view (Show user's articles)
@login_required
def dashboard_view(request):
    user = request.user
    articles = Article.objects.filter(author=user) 
    return render(request, 'dashboard.html', {'articles': articles})



@login_required
def update_profile(request):
    if not hasattr(request.user, 'profile'):
        Profile.objects.create(user=request.user)

    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('profile')  
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    return render(request, 'update_profile.html', {'user_form': user_form, 'profile_form': profile_form})



def article_detail(request, id):
    article = get_object_or_404(Article, id=id)
    comments = Comment.objects.filter(article=article)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article  
            if request.user.is_authenticated: 
                comment.user = request.user 
            comment.save()
            messages.success(request, 'Your comment has been added!')
            return redirect('article_detail', id=article.id)  
    else:
        form = CommentForm()

    for comment in comments:
        if comment.user and comment.user.profile.profile_picture:
           
            comment.profile_picture_url = comment.user.profile.profile_picture.url
        else:
           
            comment.profile_picture_url = "/static/images/default_profile.jpg" 

    return render(request, 'article_detail.html', {
        'article': article,
        'comments': comments,
        'form': form,
    })


def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    if comment.user == request.user:
        comment.delete()
        messages.success(request, 'Your comment has been deleted!')
    else:
        messages.error(request, 'You cannot delete this comment.')

    return redirect('article_detail', id=comment.article.id)


"""
def delete_comment(request, token):
    # Find the comment by its unique token
    comment = get_object_or_404(Comment, token=token)
    
    # Ensure that the user is either logged in and the comment belongs to them, or it's an anonymous comment
    if request.user == comment.user or not comment.user:
        comment.delete()
        messages.success(request, 'Your comment has been deleted.')
    else:
        messages.error(request, 'You are not authorized to delete this comment.')

    return redirect('article_detail', id=comment.article.id)"""





# views.py
from django.contrib.auth import views as auth_views
from django.shortcuts import render
from django.contrib.auth.forms import PasswordResetForm

# Custom Password Reset View
class CustomPasswordResetView(auth_views.PasswordResetView):
    template_name = 'password_reset_form.html'  # Custom template for password reset form
    email_template_name = 'password_reset_email.html'  # Custom template for the email body
    subject_template_name = 'password_reset_subject.txt'  # Custom subject for email
    success_url = '/password_reset/done/'  # Redirect after successfully submitting the form

# Custom Password Reset Done View
class CustomPasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = 'password_reset_done.html'  # Custom template for reset done page

# Custom Password Reset Confirm View
class CustomPasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = 'password_reset_confirm.html'  # Custom template for password reset confirmation page

# Custom Password Reset Complete View
class CustomPasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    template_name = 'password_reset_complete.html'  # Custom template for reset complete page



from django.core.mail import EmailMessage
from django.template.loader import render_to_string

def send_password_reset_email(user, uidb64, token):
    subject = "Password Reset Instructions"
    
    # Create the HTML message content using the template
    html_message = render_to_string('password_reset_email.html', {
        'user': user,
        'uid': uidb64,
        'token': token,
        'protocol': 'http',  # Use 'https' if you're using HTTPS
        'domain': '127.0.0.1:8000',  # Change to your domain in production
    })
    
    # The plain text version is optional but can help ensure the email works well in all email clients
    plain_message = 'This is a plain-text version of the email.'
    
    # Create email object
    email = EmailMessage(
        subject,
        plain_message,  # Plain text version
        'projectbtech752@gmail.com',  # From email address
        [user.email],  # Recipient email
    )
    
    # Attach HTML content as an alternative
    email.attach_alternative(html_message, "text/html")
    
    # Send the email
    email.send()
