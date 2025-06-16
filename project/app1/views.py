from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm, StudentForm  # FIX: Correctly import form classes
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate

list1 = [
    {"title": "title1", "text1": "Card-1 text", "price": "#usn100"},
    {"title": "title2", "text1": "Card-2 text", "price": "#usn200"},
    {"title": "title3", "text1": "Card-3 text", "price": "#usn300"}
]

def landingPageView(request):
    return render(request, 'landing.html')

def firstPageView(request):
    return render(request, 'first.html', {'li': list1})

def pricingPageView(request):
    return render(request, 'pricing.html')

def pricingPageView2(request):
    return render(request, 'pricing2.html', {'item': list1})

def indexPageView(request):
    return render(request, 'index.html')

def contactPageView(request):  # Rename to avoid confusion
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print("Form accepted")
            messages.success(request, "Response recorded")
        else:
            print("Not accepted")
            return render(request, 'contact.html', {'form_data': form})
    return render(request, 'contact.html', {'form_data': form})

def studentPageView(request):
    form = StudentForm()
    return render(request, 'student.html', {'student_data': form})

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # change to your homepage
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # change as needed
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})