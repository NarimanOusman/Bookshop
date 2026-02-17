from django.shortcuts import render, redirect

def home(request):
    return render(request, 'index.html')

def products(request):
    return render(request, 'products.html')

def register(request):
    if request.method == 'POST':
        return redirect('products')
    return redirect('home')
