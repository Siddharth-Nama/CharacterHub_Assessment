# 🧠 Backend – Django REST API

This is the **backend repository**, developed as part of the **CharacterHub 1-hour coding round**.

> **Tech Stack**: Django • Django REST Framework • SQLite • UUID Models • Token-based Auth (customizable)


🌍 Deployment
This project is deployed on PythonAnywhere
🔗 https://siddnamazeotapassessment.pythonanywhere.com/   (just go /admin/ first and then /posts/?page2)

---

## 📦 What This Backend Does

This Django-powered backend provides a secure, scalable RESTful API for:

- ✅ User-authenticated **Post creation** with UUID-based primary keys
- 📄 JSON-based API responses, paginated
- 🔐 Querysets filtered to authenticated users only
- 📆 Data stored with timestamp and user relations

---

## 🏗️ Project Structure

backend/
├── apps/
│ └── demo/
│ ├── models.py # Post & Comment models
│ ├── serializers.py # DRF Serializers
│ ├── views.py # API Views
│ └── urls.py # Endpoint routes
├── demo_project/
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
└── manage.py

yaml
Copy
Edit

---

## 📁 Models Overview

### 🔸 `Post`
```python
id         = UUID (Primary Key, auto-generated)
text       = TextField (Post content)
timestamp  = DateTimeField (auto_now_add=True)
user       = ForeignKey(User)
🔸 Comment
python
Copy
Edit
id         = UUID (Primary Key, auto-generated)
text       = TextField (Comment content)
timestamp  = DateTimeField (auto_now_add=True)
post       = ForeignKey(Post, related_name='comments')
user       = ForeignKey(User)
⚠️ Both models use UUIDField for improved security and traceability.

🔌 API Endpoints
Method	Endpoint	Description	Auth Required
GET	/posts/	List all posts created by the user	✅ Yes

You can extend this API with:

POST /posts/ – Create a new post

🔐 Authentication
This backend currently uses Django's default user model and session-based authentication. It can be easily extended to support:

Token-based Auth (via DRF's TokenAuthentication)

JWT Auth (via djangorestframework-simplejwt)

OAuth (via django-allauth)

To restrict queries to the logged-in user, this is used:

python
Copy
Edit
def get_queryset(self):
    return Post.objects.filter(user=self.request.user).order_by('-timestamp')
⚙️ Local Setup
Clone the Repo

bash
Copy
Edit
git clone https://github.com/Siddharth-Nama/CharacterHub_Assessment/
cd backend_repo
Create Virtual Environment

bash
Copy
Edit
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
Install Dependencies

bash
Copy
Edit
pip install -r requirements.txt
Run Migrations

bash
Copy
Edit
python manage.py migrate
Create Superuser (Optional)

bash
Copy
Edit
python manage.py createsuperuser
Run Server

bash
Copy
Edit
python manage.py runserver
🔗 API will be available at http://127.0.0.1:8000/posts/


✅ DRF Settings Summary
Inside settings.py:

python
Copy
Edit
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}
📌 Improvements for Production
 Add JWT Authentication using SimpleJWT

 Use PostgreSQL in production

 Add POST, PUT, DELETE methods for Posts and Comments

 Rate limiting and permissions

 API documentation with Swagger or Postman

👨‍💻 Built by Siddharth Nama
🎯 C4GT 2025 DMP Winner • Ex-Intern @ eSaral • Full Stack Dev @ IIIT Bhagalpur
📧 siddharthnama.work@gmail.com | 📱 +91 8000694996

🔁 For complete frontend + UI interaction, check out:
frontend/README.md