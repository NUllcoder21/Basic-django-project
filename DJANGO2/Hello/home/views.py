from django.shortcuts import render,HttpResponse,redirect
from datetime import datetime
from home.models import Contect
from home.models import Signup
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password, check_password


# Create your views here.
def index(request):
    context ={
        'variable':"this is variable"
    }
    
    return render(request,'index.html',context)

def about(request):
     return render(request,'about.html')
def icecream_details(request):
    return render(request, 'icecream_details.html')

def buy_now(request):
    return render(request, 'buy_now.html')

def services(request):
    return render(request,'services.html')
def contect(request):
     if request.method=="POST":
          name=request.POST.get('name')
          email=request.POST.get('email')
          phone=request.POST.get('phone')
          desc=request.POST.get('desc')
          contect = Contect(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
          contect.save()
          messages.success(request,'your message has been sent!')

     return render(request,'contect.html')
   # return HttpResponse("This is contect page")
def user_login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = Signup.objects.get(email=email)  # Fetch user by email
            if check_password(password, user.password):  # Compare hashed password
                request.session['user_id'] = user.id  # Store user ID in session
                request.session['user_name'] = user.name  # Store username
                
                messages.success(request, "Login successful!")  # Flash message
                return redirect('index')  # Redirect to home page

            else:
                messages.error(request, "Invalid email or password. Try again.")
                return redirect('user_login')

        except Signup.DoesNotExist:
            messages.error(request, "Invalid email or password. Try again.")
            return redirect('user_login')

    return render(request, 'login.html')

# Logout View
def user_logout(request):
    request.session.flush()  # Clear user session
    messages.success(request, "You have been logged out.")
    return redirect('index')

@csrf_exempt
def signup(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if user already exists
        if Signup.objects.filter(email=email).exists():
            messages.error(request, "Email already registered. Please log in.")
            return redirect('user_login')

        # Hash the password before saving
        hashed_password = make_password(password)
        signup = Signup(name=name, email=email, password=hashed_password)
        signup.save()

        messages.success(request, "Account created! Please log in.")
        return redirect('user_login')

    return render(request, 'signup.html')