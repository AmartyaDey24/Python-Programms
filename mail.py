import smtplib
import getpass

s = smtplib.SMTP('smtp.gmail.com','587')
s.starttls()
sender = 'amartyadey24@gmail.com'
reciever = 'amangnair2000@gmail.com'
mssg = "hii bro how r u"
mssg1 = MIMEMultipart()
filename = "snake2.py"
attach = "/home/al108/snake2.py"
p = getpass.getpass()
s.login(sender,p)
s.sendmail(sender,reciever,mssg)
print("mssg sent successfully")
s.quit()