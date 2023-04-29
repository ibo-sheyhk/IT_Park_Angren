from email import message
from multiprocessing import context
from pickle import NONE
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm, CreateEmployeeForm
from mainapp.models import Employee, Teacher

# Create your views here.
def mainPage(request):
    return render(request,'mainapp/index.html')
def aboutPage(request):
    return render(request,'mainapp/about.html')
def coursePage(request):
    return render(request,'mainapp/course.html')
def contactPage(request):
    return render(request,'mainapp/contact.html')
def singlePage(request):
    return render(request,'mainapp/single.html')
def teacherPage(request):
  teacher = Teacher.objects.all()
  context = {
    'teacher': teacher
  }
  return render(request,'mainapp/teacher.html', context)
def blogPage(request):
    return render(request,'mainapp/blog.html')
def studentPage(request):
    return render(request,'mainapp/student.html')
def tablePage(request):
  employees = Employee.objects.all()
  context = {
    'employees': employees,
  }
  return render(request,'mainapp/table.html',context)

def registerUser(request):
      form = CreateUserForm()
      if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                  form.save()
                  user = form.cleaned_data.get('username')
                  return redirect('about')
      context = {
        'form': form
      }
      return render(request,'mainapp/register.html',context )


def createPage(request):
    form = CreateEmployeeForm()
    if request.method == "POST":
      form = CreateEmployeeForm(request.POST) 
      if form.is_valid():
        form.save()
        return redirect('table')   
      else:
        form = CreateEmployeeForm()
        
    context = {
      'form':form
    }
    return render(request, 'mainapp/create.html', context)



# def loginPage(request):
#   if request.method == 'POST':
#     username = request.POST.get('username')
#     password = request.POST.get('password')

#     user = authenticate(request, username=username, password=password)

#     if user is not NONE:
#       login(request,user)
#       return redirect('main')
#     else:
#       message.info(request, 'Username or password was incorrect')
      
      
      
#   context = {
        
#   }  


#   return render(request, 'mainapp/login.html')



def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request,user)
            return redirect('main')
        else:
            messages.info(request, "Username or password was incorrect")
            
    context = {
        
    }   
    
    return render(request, 'mainapp/login.html')