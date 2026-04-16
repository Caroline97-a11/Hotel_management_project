from django.shortcuts import render, redirect
from .forms import StaffLoginForm, StaffForm
from .models import Staff
from django.contrib.auth import login, logout
from django.contrib.auth.hashers import make_password, check_password
# Create your views here.
def logIn(request):
    if request.method =='POST':
     form = StaffLoginForm(request, data =request.POST)
     if form.is_valid():
        userDeatils =form.get_user()
        login(request, userDeatils)
        return redirect('roomsList') 
    else:
       form =StaffLoginForm()
    return render(request, 'login.html', {'form':form})
def register(request):
    if request.method == 'POST':
        form = StaffForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form = StaffForm()

    return render(request, 'register.html', {'form': form})

# def regCopy(request):
#    register = Usar.objects.create()
#    if request.method == 'POST':
#       username = request.POST['username']
#       email = request.POST['email']
#       password = request.POST['password']
#       hashedPwd = make_password('password')

#       if Usar.objects.filter(user_name  = username).first():
#          print('user name already exists')

#       else:
#        print('user name does not exist')
#       register =Usar.objects.create(
#          user_name =username,
#          email =email,
#          password=hashedPwd
#       )
#       return redirect ('register')
#    else:
#     return render(request, 'staff/logIn.html')