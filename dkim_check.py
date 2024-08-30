import dkim
import smtplib

def sign_email(email_body, domain, selector, private_key_path):
    """
    Sign the email using DKIM.
    """
    # Prepare headers to sign
    headers = [b'from', b'to', b'subject', b'date']

    # Read the private key
    with open("/home/innuser002/private.key", 'rb') as key_file:
        private_key = key_file.read()

    # Generate DKIM signature
    dkim_signature = dkim.sign(
        message=email_body,
        selector=selector.encode(),
        domain=domain.encode(),
        privkey=private_key,
        include_headers=headers
    )

    # Add the DKIM signature to the email
    signed_email = dkim_signature + email_body
    return signed_email

def send_signed_email(signed_email, smtp_server, smtp_port, login_email, login_password, from_email, to_email):
    """
    Send the DKIM signed email using SMTP.
    """
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(login_email, login_password)
    server.sendmail(from_email, to_email, signed_email)
    server.quit()

# Email content
email_body = """From: sender@yourdomain.com
To: recipient@example.com
Subject: Urgent Hiring-Chat Process
Date: Mon, 29 Aug 2024 12:34:56 -0000

You are Invited,

Urgent Hiring-Chat Process-2,64,000 LPA salary- Fresher/Experience

Company- Concentrix

Check Your eligibility on YouTube AND come for Interview 👇👇👇

https://youtu.be/xQJ3W1gNk0Y

Join WhatsApp Group- (Mandatory)

https://chat.whatsapp.com/E0wsjknOJ61G005107azb3

DATE OF INTERVIEW 28th August 2024

TIME OF INTERVIEW - 9am to 12pm

(IT IS MANDATORY TO FOLLOW BOTH WhatsApp AND SUBSCRIBE YouTube PLATFORM)

Interview Location 👇👇👇

Gaurav Towers, 401, 1, pvr, Vikaspuri, New Delhi, Delhi 110018

Nearest metro Janakpuri EastNear Hongs Kitchen

4th Floor waiting area (3rd Floor office)

Map Location- https://g.co/kgs/TebwNVU

Contact: (Meet me only after reaching)

HR Sonu chaurasiya
9717700137
Skill Seekers Consultancy
200% Guaranty success
"""

# Convert email body to bytes
email_body_bytes = email_body.encode('utf-8')

# Sign the email
signed_email = sign_email(
    email_body=email_body_bytes,
    domain="https://mail.google.com/",  # Your domain
    selector="selector1",     # Your selector
    private_key_path="private.key"  # Path to your private key file
)

# Send the signed email
send_signed_email(
    signed_email=signed_email,
    smtp_server="smtp.gmail.com",  # Your SMTP server
    smtp_port=587,                      # SMTP port
    login_email="vandanasborate2193@gmail.com",  # Your login email
    login_password="qwcu dajw mhcb ypau",     # Your email password
    from_email="vandanasborate2193@gmail.com", # Sender email address
    to_email="vandanaborate2193@gmail.com"    # Recipient email address
)

print("DKIM signed email sent successfully.")
