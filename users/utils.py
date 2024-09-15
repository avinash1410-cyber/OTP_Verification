from twilio.rest import Client
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
        sg = SendGridAPIClient(os.getenv('SENDGRID_API_KEY'))
        
        # Send the email
        response = sg.send(message)
        
        # Print response details
        print(response.status_code)
        print(response.body)
        print(response.headers)
        
    except Exception as e:
        print(f"Error sending email: {str(e)}")

# Twilio SMS OTP sending function
def send_mobile_otp(mobile_number, otp):
    account_sid = os.getenv('TWILIO_ACCOUNT_SID')
    auth_token = os.getenv('TWILIO_AUTH_TOKEN')
    twilio_phone_number = os.getenv('TWILIO_PHONE_NUMBER')

    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=f"Your OTP is {otp}",
        from_=twilio_phone_number,
        to=mobile_number
    )
    return message.sid
