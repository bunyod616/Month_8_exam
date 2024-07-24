from django.shortcuts import render, redirect
from .forms import MoneyControlForm
from django.http import JsonResponse
from django.shortcuts import render
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from .models import MoneyControl
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from datetime import timedelta
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _

User = get_user_model()


def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return redirect("index")

        return redirect("login")

    return render(request, "auth/login.html")


def logout_user(request):
    logout(request)
    return redirect("login")


def register_user(request):
    if request.POST:
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if username and password1 and password2 and password1 == password2:
            user = User.objects.create(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
            )
            user.set_password(password2)
            user.save()
            return redirect("login")

    return render(request, "auth/register.html")



def index(request):
    if not request.user.is_authenticated:
        return redirect("login")
    transactions = MoneyControl.objects.all()
    total_income = sum(t.amount for t in transactions if t.type == 'IN')
    total_expense = sum(t.amount for t in transactions if t.type == 'OUT')
    balance = total_income - total_expense
    context = {
        'transactions': transactions,
        'total_income': total_income,
        'total_expense': total_expense,
        'balance': balance,
    }
    return render(request, 'index.html', context)

def reports(request):
    user = request.user
    transactions = MoneyControl.objects.filter(user=user)
    total_income = sum(t.amount for t in transactions if t.type == 'IN')
    total_expense = sum(t.amount for t in transactions if t.type == 'OUT')
    balance = total_income - total_expense

    context = {
        'total_income': total_income,
        'total_expense': total_expense,
        'balance': balance,
    }
    return render(request, 'reports.html', context)


def filling(request):
    if request.method == 'POST':
        form = MoneyControlForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            return redirect('index')
    else:
        form = MoneyControlForm()
    return render(request, 'filling_money.html', {'form': form})





def daily_stats(request):
    user = request.user
    today = now().date()
    start_of_day = today
    end_of_day = start_of_day + timedelta(days=1)

    daily_income = MoneyControl.objects.filter(
        user=user, type='IN', date__range=[start_of_day, end_of_day]
    ).aggregate(total_income=Sum('amount'))['total_income'] or 0

    daily_expense = MoneyControl.objects.filter(
        user=user, type='OUT', date__range=[start_of_day, end_of_day]
    ).aggregate(total_expense=Sum('amount'))['total_expense'] or 0


    return JsonResponse({
        'daily_income': daily_income,
        'daily_expense': daily_expense,
    })

def weekly_stats(request):
    user = request.user
    today = now().date()
    start_of_week = today - timedelta(days=today.weekday())
    end_of_week = start_of_week + timedelta(days=7)

    weekly_income = MoneyControl.objects.filter(
        user=user, type='IN', date__range=[start_of_week, end_of_week]
    ).aggregate(total_income=Sum('amount'))['total_income'] or 0

    weekly_expense = MoneyControl.objects.filter(
        user=user, type='OUT', date__range=[start_of_week, end_of_week]
    ).aggregate(total_expense=Sum('amount'))['total_expense'] or 0

    return JsonResponse({
        'weekly_income': weekly_income,
        'weekly_expense': weekly_expense,
    })


def monthly_stats(request):
    user = request.user
    today = now().date()
    start_of_month = today.replace(day=1)
    end_of_month = (start_of_month + timedelta(days=31)).replace(day=1)

    monthly_income = MoneyControl.objects.filter(
        user=user, type='IN', date__range=[start_of_month, end_of_month]
    ).aggregate(total_income=Sum('amount'))['total_income'] or 0

    monthly_expense = MoneyControl.objects.filter(
        user=user, type='OUT', date__range=[start_of_month, end_of_month]
    ).aggregate(total_expense=Sum('amount'))['total_expense'] or 0

    return JsonResponse({
        'monthly_income': monthly_income,
        'monthly_expense': monthly_expense,

    })
