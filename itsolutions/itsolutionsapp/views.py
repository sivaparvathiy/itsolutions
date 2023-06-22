from django.shortcuts import render, redirect
from .models import AdminData, studentsData, studentfeedbackData
from .forms import RegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

def Adminloginview(request):
    if request.method == 'POST':
        username = request.POST['Aunames']
        password = request.POST['Aupass']
        users = authenticate(username = username,password = password)
        if users is not None:
            login(request,users)
            return redirect(Adminhomeview)
        else:
            return HttpResponse('invaild')
    else:
        return render(request, 'index.html')

def Studentloginview(request):
    if request.method == 'POST':
        usernames = request.POST['Suname']
        password = request.POST['Supass']
        user = authenticate(username = usernames,password = password)
        if user is not None:
            login(request,user)
            return redirect(Studenthomeview)
        else:
            return HttpResponse('invaild')
    else:
        return render(request, 'index.html')

@login_required(login_url='logins')
def Adminhomeview(request):
    return render(request, 'home.html')

@login_required(login_url='slogins')
def Studenthomeview(request):
    return render(request, 'studenthome.html')

@login_required(login_url='logins')
def adminform(request):
    if request.method == 'GET':
        return render(request,'adminform.html')
    else:
        AdminData(
        course_name = request.POST['cname'],
        fee = request.POST['fee'],
        institute = request.POST['institue'],
        trainer_name = request.POST['tname'],
        date = request.POST['date'],
        trainer_mode = request.POST['tmode']
        ).save()
        return redirect(adminform)


def studentform(request):
    if request.method == 'GET':
        return render(request,'studentform.html')
    else:
        studentsData(
        first_name = request.POST['fname'],
        last_name = request.POST['lname'],
        email_id = request.POST['institue'],
        mobile = request.POST['mobile'],
        course = request.POST['course'],
        qualification = request.POST['qualification'],
        location = request.POST['location'],
        ).save()
        return redirect(studentform)

def studentservicesview(request):
    data = AdminData.objects.all()
    return render(request, 'studentservices.html',{'data': data})

@login_required(login_url='logins')
def studentinformation(request):
    data = studentsData.objects.all()
    return render(request, 'sinformation.html', {'data': data})

def Adminlogoutview(request):
    logout(request)
    return redirect(Adminloginview)

def studentfeedbackview(request):
    if request.method == 'GET':
        data = studentfeedbackData.objects.all().order_by('-id')
        return render(request, 'studentfeedbackform.html',{'data':data})
    else:
        studentfeedbackData(
        user_name = request.POST['uname'],
        comment = request.POST['comment'],
        date = request.POST['dt'],
        ).save()
        return redirect(studentfeedbackview)

def student_comment_to_admin(request):
    data = studentfeedbackData.objects.all().order_by('-id')
    return render(request, 'scta.html',{'data':data})

def delete_student_comment(request,id):
    data = studentfeedbackData.objects.get(id=id)
    data.delete()
    return redirect(studentfeedbackview)
def galleryviews(request):
    return render(request,'admingallery.html')


def registerview(request):
    if request.method == 'GET':
        form=RegistrationForm()
        return render(request,'registerform.html',{'form':form})
    else:
        form=RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            form.save()
            return redirect(Adminloginview)
        else:
            return HttpResponse("invalid form")
