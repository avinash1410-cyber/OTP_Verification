from django.shortcuts import render, redirect
from .models import CustomUser, OTP
from .utils import send_mobile_otp, send_email_otp
from django.shortcuts import render, redirect
from .models import CustomUser, OTP
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages


@login_required
def profile_view(request):
    return render(request, 'profile.html')





def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')  # Redirect to the home page after login
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')








def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        mobile_number = request.POST.get('mobile_number')
        username = request.POST.get('username')

        # Temporarily store the user information in the session
        request.session['email'] = email
        request.session['mobile_number'] = mobile_number
        request.session['username'] = username

        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

        print(email)
        print(mobile_number)
        print(username)


        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")



        # Generate and send email OTP
        email_otp = OTP.objects.create(otp_type='email')
        email_otp.generate_otp()
        print(email_otp.otp_code)  # This should print the generated OTP
        print("EMAILEMAILEMAILEMAILEMAILEMAILEMAILEMAILEMAILEMAIL")
        email_otp.save()
        send_email_otp(email, email_otp.otp_code)

        # Generate and send mobile OTP
        mobile_otp = OTP.objects.create(otp_type='mobile')
        mobile_otp.generate_otp()
        print(mobile_otp.otp_code)  # This should print the generated OTP
        print("PHONEPHONEPHONEPHONEPHONEPHONEPHONEPHONEPHONE")
        mobile_otp.save()
        send_mobile_otp(mobile_number, mobile_otp.otp_code)

        # Store the OTPs in the session
        request.session['email_otp_id'] = email_otp.id
        request.session['mobile_otp_id'] = mobile_otp.id

        # Redirect to OTP verification page
        return redirect('verify_otp')
    return render(request, 'register.html')








def verify_otp(request):
    email = request.session.get('email')
    mobile_number = request.session.get('mobile_number')
    email_otp_id = request.session.get('email_otp_id')
    mobile_otp_id = request.session.get('mobile_otp_id')
    username = request.session.get('username')

    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    
    print(email)
    print(mobile_number)
    print(email_otp_id)
    print(mobile_otp_id)
    email_otp=OTP.objects.get(id=email_otp_id)
    mobile_otp=OTP.objects.get(id=mobile_otp_id)
    print(email_otp)
    print(mobile_otp)


    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    

    if request.method == 'POST':
        email_otp_input = request.POST.get('email_otp')
        mobile_otp_input = request.POST.get('mobile_otp')

        # Retrieve OTPs from the database
        email_otp = OTP.objects.get(id=email_otp_id)
        mobile_otp = OTP.objects.get(id=mobile_otp_id)
        password = request.POST.get('password')

        # Verify email OTP
        if email_otp and email_otp.otp_code == email_otp_input or mobile_otp.otp_code==email_otp_input:
            email_verified = True
            print("Successfully verified Email OTP")
        else:
            print("Email OTP is invalid")
            return render(request, 'verify_otp.html', {'error': 'Invalid email OTP'})

        # Verify mobile OTP
        if mobile_otp and mobile_otp.otp_code == mobile_otp_input:
            print("Successfully verified Mobile OTP")
            mobile_verified = True
        else:
            print("Mobile OTP is invalid")
            return render(request, 'verify_otp.html', {'error': 'Invalid mobile OTP'})

        # If both OTPs are verified, create the user
        if email_verified or mobile_verified:
            user = CustomUser.objects.create_user(
                username=username,
                email=email,
                mobile_number=mobile_number,
                password=password
            )
            user.save()

            # Clear session data
            request.session.flush()
            # Redirect to success page
            return redirect('success')
    return render(request, 'verify_otp.html')









def success(request):
    return render(request, 'success.html')