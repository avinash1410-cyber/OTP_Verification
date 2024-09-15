# users/utils.py

from twilio.rest import Client
import sendgrid
from sendgrid.helpers.mail import Mail
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

import os















# SendGrid email OTP sending function
def send_email_otp(email, otp):
    print("In Email OTP Send")
    
    # Create email message
    message = Mail(
        from_email=os.getenv('DEFAULT_FROM_EMAIL', 'avi8654340@gmail.com'),
        to_emails=email,
        subject='Your Email OTP',
        html_content=f'<strong>Your OTP is {otp}</strong>'
    )
    
    try:
        # Initialize SendGrid client with API key
        sg = SendGridAPIClient(os.getenv('sendgrid_id'))
        
        # Send the email
        response = sg.send(message)
        
        # Print response details
        print(response.status_code)
        print(response.body)
        print(response.headers)
        
    except Exception as e:
        print(f"Error sending email: {str(e)}")






#Dummy

# users/utils.py

# Dummy SMS OTP sending function
# def send_mobile_otp(mobile_number, otp):
#     print(f"Sending SMS OTP to {mobile_number}: {otp}")
#     return 200  # Simulate a response ID

# Dummy email OTP sending function
# def send_email_otp(email, otp):
#     print(f"Sending Email OTP to {email}: {otp}")
#     return 200  # Simulate a successful HTTP status code




# Twilio SMS OTP sending function
def send_mobile_otp(mobile_number, otp):
    account_sid = os.getenv('account_sid')
    auth_token = os.getenv('auth_token')
    twilio_phone_number = os.getenv('twilio_phone_number')

    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=f"Your OTP is {otp}",
        from_=twilio_phone_number,
        to=mobile_number
    )
    return message.sid
