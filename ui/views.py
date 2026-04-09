from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.shortcuts import render

MOCK_STATS = {
    'users_21_30': 128,
    'users_with_job': 76,
    'users_with_age_and_job': 70,
    'users_in_it': 54,
    'users_in_partners': 19,
    'top_companies': [('Axenix', 6), ('Т-Банк', 4), ('SimbirSoft', 3), ('Портал-Юг', 3)],
    'geo': {
        'Axenix': [('Краснодар', 3), ('Москва', 2), ('Санкт-Петербург', 1)],
        'Т-Банк': [('Москва', 2), ('Краснодар', 2)],
    },
}
MOCK_ACHIEVEMENTS = [
    {'student': 'Иван Петров', 'type': 'Хакатон', 'title': 'AI Hack 2025', 'place': '1 место'},
    {'student': 'Мария Сидорова', 'type': 'Чемпионат', 'title': 'Data Cup', 'place': '2 место'},
]
MOCK_USERS = [
    {'fio': 'Иван Петров', 'city': 'Краснодар', 'has_job': 'Да', 'job': 'Axenix'},
    {'fio': 'Мария Сидорова', 'city': 'Москва', 'has_job': 'Да', 'job': 'Т-Банк'},
]

def is_admin(user):
    return user.is_superuser

@login_required(login_url='account_login')
def home_view(request):
    return render(request, 'ui/home.html')

@login_required(login_url='account_login')
def stats_view(request):
    return render(request, 'ui/stats.html', MOCK_STATS)

@login_required(login_url='account_login')
def achievements_view(request):
    return render(request, 'ui/achievements.html', {'achievements': MOCK_ACHIEVEMENTS})

@login_required(login_url='account_login')
def users_view(request):
    return render(request, 'ui/users.html', {'users': MOCK_USERS})

@user_passes_test(is_admin)
def system_users_view(request):
    users = User.objects.all().order_by('email')
    return render(request, 'ui/system_users.html', {'users': users})
