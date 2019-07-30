from django.http import HttpResponse
from django.shortcuts import render, redirect
import math
from .models import *
from .forms import *
from twilio.rest import Client
import random


# Create your views here.

def one(request) :
    return render(request, 'index.html')


def about(request) :
    return render(request, 'about.html')


def project(request) :
    return render(request, 'project.html')


def testimonial(request) :
    return render(request, 'testimonial.html')


def blog(request) :
    msg = ''
    if request.method == 'POST' :
        num = int(request.POST.get('number'))

        if num < 0 :
            msg = "Sorry, factorial does not exist for negative numbers"
        elif num == 0 :
            msg = "The factorial of 0 is 1"
        else :
            factorial = math.factorial(num)
            msg = "The factorial of " + str(num) + " is " + str(factorial)

    return render(request, 'blog.html', {'msg' : msg})


def add(request) :
    form = firstform(request.POST)
    if request.method == 'POST' :
        if form.is_valid() :
            form.save()
            return redirect(new)
    return render(request, 'addstudent.html', {'form' : form})


def new(request) :
    ob = Student.objects.all()
    return render(request, 'new.html', {'obj' : ob})


def delete(request, id) :
    ab = Student.objects.get(id=id)
    ab.delete()
    return redirect(new)


def edit(request, id) :
    abc = Student.objects.get(id=id)
    form = firstform(request.POST or None, instance=abc)
    if request.method == 'POST' :
        if form.is_valid() :
            form.save()
            return redirect(new)

    return render(request, 'addstudent.html', {'form' : form})


def signup(request) :
    form = signupform(request.POST)
    if request.method == 'POST' :
        if form.is_valid() :
            print("yes...")
            form.save()
            no = form.cleaned_data.get('number')
            otp_g = random.randint(1000, 9999)
            request.session['otp_g'] = otp_g
            print(otp_g)
            a = "ACd0310c98f582e1231f79acbeeae8bfa5"
            b = "bd8c5a962a98506d6701b2fd24cfba42"
            abc = Client(a, b)
            abc.messages.create(from_="(202) 915-7785", to="91"+str(no),
                                body="hai...your verification code is " + str(otp_g))
        return redirect(otp)
    return render(request, 'signup.html', {'form' : form})


def table(request) :
    ac = Auth.objects.all()
    return render(request, 'signupsave.html', {'ab' : ac})


def delet(request, id) :
    ab = Auth.objects.get(id=id)
    ab.delete()
    return redirect(table)


def edi(request, id) :
    a = Auth.objects.get(id=id)
    form = signupform(request.POST or None, instance=a)
    if request.method == 'POST' :
        if form.is_valid() :
            form.save()

            return redirect(table)

    return render(request, 'signup.html', {'form' : form})


def login(request) :
    msg = ""
    if request.method == 'POST' :
        u = request.POST.get('uname')
        p = request.POST.get('psw')
        try :
            abc = Auth.objects.get(username=u, password=p)
            if abc is not None :
                return redirect(one)
        except :
            msg = "Invalid user....Try sign Up...."
    return render(request, 'login.html', {'msg' : msg})

def otp(request):
    msg = ""
    otp_g = request.session['otp_g']
    print(otp_g)
    if request.method == 'POST':
        otp_e = request.POST.get('otp')
        if int(otp_e) == otp_g:
            return redirect(one)
        else:
            msg = "OTP Incorrect..."
    return render(request, 'otp.html', {'msg': msg})


def hotel_image_view(request):
    if request.method == 'POST':
        form = HotelForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('success')
    else :
        form = HotelForm()
    return render(request, 'image_app.html', {'form' : form})


def success(request) :
    return HttpResponse('successfuly uploaded')


def display_hotel_images(request):
    if request.method == 'GET':

        Hotels = Hotel.objects.all()
        return render(request, 'display.html',{'hotel_images': Hotels})

def logout(request):
    return redirect(login)