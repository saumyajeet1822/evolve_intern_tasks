"""OTP Verification using Python

First, create a 6-digit random number.

Then store the number in a variable.
Then we need to write a program to send emails.
When sending email, we need to use OTP as a message.
Finally, we need to request two user inputs; first for the user’s email and then for the OTP that the user has received.
To generate a 6-digit OTP and send it via email for verification, we will use the random library . The stmplib library to send the email. For this example, we'll use a Gmail account to send the email. Remember to replace your mail id

Here's the Python program:
"""

import random
import string
import smtplib

def generate_otp():
    digits = string.digits
    otp = ''.join(random.choice(digits) for i in range(6))
    return otp

def send_otp_email(email, otp):
    from_email = 'your_email@gmail.com'  # Replace with your Gmail email address
    from_password = 'your_email_password'  # Replace with your Gmail password

    subject = 'OTP Verification'
    message = f'Your OTP for verification is: {otp}'

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(from_email, from_password)

        server.sendmail(from_email, email, f'Subject: {subject}\n\n{message}')
        print('OTP sent successfully!')

        server.quit()
    except Exception as e:
        print(f"Error: {e}")

def main():
    email = input('Enter your email address: ')
    otp = generate_otp()
    print(f"Generated OTP: {otp}")

    send_otp_email(email, otp)

    user_otp_input = input('Enter the OTP you received: ')

    if user_otp_input == otp:
        print('OTP verification successful. Account created!')
    else:
        print('Invalid OTP. Verification failed.')

if __name__ == "__main__":
    main()