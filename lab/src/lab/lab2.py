import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def mailotp(otp,id):
    sender_email = "vyshnavmohan20@gmail.com"
    password = "dszi evmt npul xpga"
    ref=dbs()
    stud=ref.child("Student").get()
    for i,j in stud.items():
        if(i==id):
            name=j['Name']
            receiver_email=j['Email']
    subject = "Your OTP for Password Reset"
    body = body = f"""\
<html>
  <body>
    <h3>Dear {name},</h3>
    <p>Please use the following One-Time Password (OTP) to reset your account password:</p>
    <h3>Your OTP: {otp}</h3>
    <p>If you did not request a password reset, please ignore this email or contact our support team.</p>
    <br>
    <h3>Best regards,<br>Department of Computer Applications,<br>College of Engineering, Trivandrum</h3>
  </body>
</html>
"""
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "html"))
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, password)
        text = message.as_string()
        server.sendmail(sender_email, receiver_email, text)
        
    except Exception as e:
        print(f"Error: {e}")
        
    finally:
        server.quit()


def update_pass(u,p):
    ref=dbs()
    stud=ref.child("Student")
    stud.update({
    u:{"Password":p}
})