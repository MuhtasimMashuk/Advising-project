from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import warning #table access korar jonno
# Create your views here.
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import eva
data=[
{'name':'Mashuk',
 'topic':'Habijabi',


},
{'name':'GHashuk',
 'topic':'kabijabi',
}


]
def home(request):
    montext ={'ata':data}
    return render(request,'evaluation/home.html',montext)
    


def form(request):
    if request.method=='POST':
        uni_id=request.POST['uni_id']
        password=request.POST['password']
        user=auth.authenticate(username=uni_id,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('evaluation-index')
        else:
            messages.info(request,'invalid')
            return redirect('evaluation-form')

    else:
        
        return render(request,'evaluation/form.html')
#for notice bord
def index(request):
    warning_data=warning.objects.all #database er warning table theke data varible e nilam

    return render(request,'evaluation/index.html',{'warning_data': warning_data})


def regi(request):

    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        uni_id=request.POST['uni_id']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']
        email=request.POST['email']
        if password==confirm_password:
            if User.objects.filter(username=uni_id).exists():
                messages.info(request,'uni_id is taken')
                return redirect('evaluation-regi')
            elif User.objects.filter(email=email).exists(): 
                 messages.info(request,'email is taken')
                 return redirect('evaluation-regi')
            else:

                
                user= User.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=uni_id,password=password)
                user.save();
                messages.info(request,'user created')
                return redirect('evaluation-regi')
        else:
            messages.info(request,'paswword is not matching')
            return redirect('evaluation-regi')
        
        return redirect('/')
    else:
         return render(request,'evaluation/regi.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def faculty(request):
    if request.method == 'POST':
         if request.POST.get('faculty_name') and request.POST.get('faculty_id'):
            evaluation=eva()
            evaluation.faculty_name= request.POST.get('faculty_name')
            evaluation.faculty_id= request.POST.get('faculty_id')
            evaluation.field1=request.POST.get('Behaviour')
            evaluation.field2=request.POST.get('teaching-style')
            evaluation.field3=request.POST.get('Giving-feedback')

            evaluation.field4=request.POST.get('Office-hour')
            evaluation.field=request.POST.get('Skill')
            evaluation.comment=request.POST.get('comment')


            evaluation.save()
             
            return render(request, 'evaluation/index.html')  

    else:
        return render(request,'evaluation/faculty.html')