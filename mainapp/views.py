from django.shortcuts import render,redirect
import urllib.request
import urllib.parse
import random 
import ssl
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from mainapp.models import *
# Create your views here.
def sendSMS(user, otp, mobile):
    data = urllib.parse.urlencode({
        'username': 'Codebook',
        'apikey': '56dbbdc9cea86b276f6c',
        'mobile': mobile,
        'message': f'Hello {user}, your OTP for account activation is {otp}. This message is generated from https://www.codebook.in server. Thank you',
        'senderid': 'CODEBK'
    })
    data = data.encode('utf-8')
    # Disable SSL certificate verification
    context = ssl._create_unverified_context()
    request = urllib.request.Request("https://smslogin.co/v3/api.php?")
    f = urllib.request.urlopen(request, data,context=context)
    return f.read()
def main_homepage(request):
    return render(request,'main/main_homepage.html')
def user_login(request):
    if request.method == 'POST':
        u_email = request.POST.get('email')
        u_password = request.POST.get('password')
        print( u_email,u_password)
        
        user_data = User_details.objects.get(Email = u_email)
        print(user_data)
        if user_data.Password == u_password:
            if user_data.Otp_Status == 'verified' and user_data.User_Status=='accepted':
                request.session['User_id'] = user_data.User_id
                messages.success(request, 'You are logged in..')
                user_data.No_Of_Times_Login += 1
                user_data.save()
                return redirect('user_dashboard')
            elif user_data.Otp_Status == 'verified' and user_data.User_Status=='pending':
                messages.info(request, 'Your Status is in pending')
                return redirect('user_login')
            else:
                messages.warning(request, 'verifyOTP...!')
                request.session['User_id'] = user_data.User_id
                return redirect('otp')
        else:
            messages.error(request, 'incorrect credentials...!')
            return redirect('user_login')
    return render(request,'main/main_user.html')
def admin_login(request):
    admin_name = 'admin'
    admin_pwd = 'admin'
    if request.method == 'POST':
        admin_n = request.POST.get('email')
        admin_p = request.POST.get('password')
        if (admin_n == admin_name and admin_p == admin_pwd):
            messages.success(request, 'You are logged in..')
            return redirect('admin_dashboard')
        else:
            messages.error(request, 'You are trying to loging with wrong details..')
            return redirect('admin_login')
    return render(request,'main/main_admin.html')
def aboutus(request):
    return render(request,'main/main_about.html')
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        User_details.objects.create(Full_name = name, Email=email, Message=message)
        messages.success(request, 'Your message has been submitted successfully.')
        return redirect('contact') 

    return render(request,'main/main_contact.html')
def register(request):
    if request.method == 'POST' :
        name = request.POST.get('name')
        age = request.POST.get('age')
        password = request.POST.get('password')
        phone = request.POST.get('mobile')
        email = request.POST.get('email')
        address = request.POST.get("address")
        image = request.FILES['image']
        print(name,age,password,phone,email,address,image)
        image = request.FILES['image']
        number = random.randint(1000,9999)
        
        print(number)
        try:
            user_data = User_details.objects.get(Email = email)
            messages.warning(request, 'Email was already registered, choose another email..!')
            return redirect("register")
        except:
            sendSMS(name,number,phone)
            User_details.objects.create(Full_name = name, Image = image, Age = age, Password = password, Address = address, Email = email, Phone_Number = phone, Otp_Num = number)
            mail_message = f'Registration Successfully\n Your 4 digit Pin is below\n {number}'
            print(mail_message)
            send_mail("User Password", mail_message , settings.EMAIL_HOST_USER, [email])
            request.session['Email'] = email
            messages.success(request, 'Your account was created..')
            return redirect('otp')
    return render(request,'main/main_register.html')
def otp(request):
    user = request.session['Email']
    user_o = User_details.objects.get(Email = user)
    print(user_o.Otp_Num,'data otp')
    if request.method == 'POST':
        user_otp = request.POST.get('otp')
        u_otp = int(user_otp)
        if u_otp == user_o.Otp_Num:
            user_o.Otp_Status = 'verified'
            user_o.save()
            messages.success(request, 'OTP verification was Success. Now you can continue to login..!')
            return redirect('main_homepage')
        else:
            messages.error(request, 'OTP verification was Faild. You entered invalid OTP..!')
            return redirect('otp')
    return render(request,'main/main_otp.html')
def forgotpwd(request):
    return render(request,'main/main_forgotpassword.html')