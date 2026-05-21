from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("school-search/", views.school_search, name="school_search"),
    path("school-results/", views.school_results, name="school_results"),
    path("choose-action/", views.choose_action, name="choose_action"),
    path("choose-rate/", views.choose_rate, name="choose_rate"),
    path("choose-check/", views.choose_check, name="choose_check"),
    path("professors/", views.professors, name="professors"),
    path("professor-detail/", views.professor_detail, name="professor_detail"),
    path("programmes/", views.programmes, name="programmes"),
    path("programme-detail/", views.programme_detail, name="programme_detail"),
    path("rate-professor/", views.rate_professor, name="rate_professor"),
    path("rate-programme/", views.rate_programme, name="rate_programme"),
    path("register/", views.register, name="register"),
    path("user-register/", views.user_register, name="user_register"),
    path("contact/", views.contact, name="contact"),
    path("submitted/", views.submitted, name="submitted"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("api/reviews/", views.api_reviews, name="api_reviews"),
]
