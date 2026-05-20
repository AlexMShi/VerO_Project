# Ver·O Student Review Platform

Ver·O is a Django-based student review platform prototype for schools, professors, and academic programmes.

## Features

- Multi-page student review platform
- Django routing for all pages
- Bootstrap responsive layout
- JavaScript interactions for search, rating, sorting, and local review storage
- Contact form connected to a Django backend
- Email sending via Gmail SMTP
- REST API endpoint at `/api/reviews/`
- Dashboard page at `/dashboard/`
- Basic security practice with CSRF token and environment variables

## Project structure

```text
VerO_project/
├── manage.py
├── core/
│   ├── views.py
│   ├── urls.py
│   └── email_utils.py
├── templates/
├── static/
├── Vero_project/
│   ├── settings.py
│   └── urls.py
├── requirements.txt
├── .gitignore
└── README.md