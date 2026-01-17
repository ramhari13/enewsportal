
# 📰 E-News Portal (Django)

A college-centered **E-News Portal Web Application** developed using **Python and Django** to provide real-time updates on academic events, placements, sports, and cultural activities.  
This platform centralizes campus communication and enhances engagement through a secure, responsive, and user-friendly interface.

---

## 📌 Project Overview

In many colleges, important information is scattered across notice boards, emails, WhatsApp groups, and social media. This often leads to missed or delayed updates.  
The **E-News Portal** solves this problem by providing a **single centralized platform** where students, faculty, and staff can access all campus-related news in real time.

---

## 🚀 Features

### 👤 User Features
- User Registration & Login (Django Authentication)
- Personalized User Profile & Dashboard
- View Breaking News & Top Headlines
- Browse News by Categories:
  - Academics
  - Placements
  - Sports
  - Events
- Create, Read, Update, Delete (CRUD) News Articles
- Comment and provide feedback on articles
- Search and filter news by keywords and categories

### 🛠️ Admin Features
- Secure Admin Login
- Admin Dashboard
- Manage Users
- Add, Edit, Delete News Articles
- Manage News Categories
- Content Moderation
- Upload Images and Media Files

---

## 🧰 Technology Stack

### Frontend
- HTML5
- CSS3
- Bootstrap 5

### Backend
- Python 3.x
- Django 4.x

### Database
- SQLite (Development)
- MySQL / PostgreSQL (Production-ready)

---

## 📁 Project Structure
# EnewsPortal 

enewsportal/
│
├── manage.py
├── db.sqlite3
├── requirements.txt
├── README.md
│
├── Enewsportal/
│ ├── init.py
│ ├── settings.py
│ ├── urls.py
│ ├── asgi.py
│ └── wsgi.py
│
├── news/
│ ├── migrations/
│ ├── static/
│ ├── templates/
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── form.py
│ ├── models.py
│ ├── views.py
│ └── tests.py
│
├── media/
│ ├── articles/
│ ├── category_images/
│ └── profile_pictures/

yaml
---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/enewsportal.git
cd enewsportal

2️⃣ Create Virtual Environment (Optional but Recommended)
python -m venv venv
source venv/bin/activate   # For Linux/macOS
venv\Scripts\activate      # For Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Apply Migrations
python manage.py migrate

5️⃣ Create Superuser (Admin)
python manage.py createsuperuser

6️⃣ Run Development Server
python manage.py runserver


Open your browser and visit:

http://127.0.0.1:8000/

🔐 Admin Panel Access
http://127.0.0.1:8000/admin/
