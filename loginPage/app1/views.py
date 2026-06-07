from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
import random

# Create your views here.
def signup(request):
    if request.method == "POST":
        username = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        return redirect('login')

    return render(request, 'signup.html')

def login_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user_obj = User.objects.get(email=email)
            username = user_obj.username
        except User.DoesNotExist:
            return render(request, 'login.html', {'error': 'User not found'})
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')


def forgot_password(request):
    if request.method == "POST":
        email = request.POST.get('email')

        try:
            user = User.objects.get(email=email)

            otp = random.randint(100000, 999999)

            request.session['otp'] = str(otp)
            request.session['email'] = email

            send_mail(
                'Password Reset OTP',
                f'Your OTP is: {otp}',
                'yourgmail@gmail.com',
                [email],
                fail_silently=False
            )

            return redirect('verify_otp')

        except User.DoesNotExist:
            return render(request, 'forgot_password.html', {
                'error': 'Email not found'
            })

    return render(request, 'forgot_password.html')

def verify_otp(request):
    if request.method == "POST":
        user_otp = request.POST.get('otp')

        if user_otp == request.session.get('otp'):
            return redirect('reset_password')
        else:
            return render(request, 'verify_otp.html', {
                'error': 'Invalid OTP'
            })

    return render(request, 'verify_otp.html')

def reset_password(request):
    if request.method == "POST":
        password = request.POST.get('password')

        email = request.session.get('email')

        user = User.objects.get(email=email)
        user.set_password(password)
        user.save()

        return redirect('login')

    return render(request, 'reset_password.html')

def home(request):
    return render(request, 'home.html')