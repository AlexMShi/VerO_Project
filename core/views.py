from django.shortcuts import render, redirect
from django.http import JsonResponse

from django.conf import settings
from .email_utils import send_email

def home(request):
    return render(request, "index.html")


def school_search(request):
    return render(request, "school-search.html")


def school_results(request):
    return render(request, "school-results.html")


def choose_action(request):
    return render(request, "choose-action.html")


def choose_rate(request):
    return render(request, "choose-rate.html")


def choose_check(request):
    return render(request, "choose-check.html")


def professors(request):
    return render(request, "professors.html")


def professor_detail(request):
    return render(request, "professor-detail.html")


def programmes(request):
    return render(request, "programmes.html")


def programme_detail(request):
    return render(request, "programme-detail.html")


def rate_professor(request):
    return render(request, "rate-professor.html")


def rate_programme(request):
    return render(request, "rate-programme.html")


def register(request):
    return render(request, "register.html")


def submitted(request):
    return render(request, "submitted.html")


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        body = f"""
New contact form message from Ver·O

Name: {name}
Email: {email}

Message:
{message}
"""

        send_email(
            to_email=settings.SMTP_USER,  
            subject="New Ver·O contact form message",
            body=body,
            reply_to=email,
        )

        return redirect("submitted")

    return render(request, "contact.html")


def dashboard(request):
    context = {
        "total_reviews": 72,
        "average_rating": 4.3,
        "total_professors": 18,
        "total_programmes": 6,
        "recent_reviews": [
            {
                "type": "Professor",
                "name": "Dr. Anna Müller",
                "rating": 4.6,
                "comment": "Clear explanations and helpful feedback."
            },
            {
                "type": "Programme",
                "name": "MSc Data Science & AI",
                "rating": 4.4,
                "comment": "Good balance between business and technical content."
            },
            {
                "type": "Professor",
                "name": "Prof. James Carter",
                "rating": 4.2,
                "comment": "Well-structured lectures and practical examples."
            }
        ]
    }

    return render(request, "dashboard.html", context)


def api_reviews(request):
    data = [
        {
            "id": 1,
            "type": "Professor",
            "name": "Dr. Anna Müller",
            "school": "emlyon business school",
            "rating": 4.6,
            "review_count": 18,
            "category": "Data Science"
        },
        {
            "id": 2,
            "type": "Professor",
            "name": "Prof. James Carter",
            "school": "emlyon business school",
            "rating": 4.2,
            "review_count": 11,
            "category": "Marketing"
        },
        {
            "id": 3,
            "type": "Programme",
            "name": "MSc Data Science & AI",
            "school": "emlyon business school",
            "rating": 4.4,
            "review_count": 24,
            "category": "Programme"
        },
        {
            "id": 4,
            "type": "Programme",
            "name": "MSc Digital Marketing & Data Analytics",
            "school": "emlyon business school",
            "rating": 4.1,
            "review_count": 19,
            "category": "Programme"
        }
    ]

    return JsonResponse(data, safe=False)