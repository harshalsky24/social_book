from django.shortcuts import render,redirect
from .forms import RegisterForm, LoginForm , UploadFileForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .models import UploadedFiles
from .db_engine import engine
from sqlalchemy import text
from django.http import JsonResponse

User = get_user_model()

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Account Create Successfully")
            return redirect('login')
    else:
        form = RegisterForm()
        return render(request,'accounts/register.html',{'form':form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            print(user)
            if user is not None:
                    login(request, user)
                    #messages.success(request, 'Logged in successfully!')
                    return redirect('upload_books') 
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Form validation failed.')
    else:
        form = LoginForm()
    
    return render(request, 'accounts/login.html', {'form': form})
        
def user_logout(request):
    logout(request)
    messages.info(request, 'Logged out successfully')
    return redirect('login')


def authors_and_sellers(request):
    public_users = User.objects.filter(public_visibility= True)
    return render(request, 'accounts/authors_and_sellers.html',{'public_users':public_users})

@login_required
def upload_books(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.save(commit=False)
            uploaded_file.user = request.user  
            uploaded_file.save()  
            #messages.success(request, 'Book uploaded successfully!')
            return redirect('uploaded_files')  
        else:
            messages.error(request, 'Invalid form submission. Please check the form.')
    else:
        form = UploadFileForm()
    
    return render(request, 'accounts/upload_books.html', {'form': form})

@login_required
def uploaded_files(request):
    files = UploadedFiles.objects.filter(user=request.user)
    return render(request,'accounts/uploaded_files.html',{'files':files})


def fetch_books(request):
    try:
        query =text("SELECT * FROM accounts_uploadedfiles")

        with engine.connect() as connection:
            result = connection.execute(query)
            books = [dict(row._mapping) for row in result]
            return JsonResponse({'books':books}, status=200)
    except Exception as e:
        return JsonResponse({'error':str(e)},status=500)    