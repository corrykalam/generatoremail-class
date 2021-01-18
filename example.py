from mail_class import *

mail = generatorEmail()

email = mail.getRandomEmail()
print(email)#rmuhammad.mubashk@bflier.com
mailbox = mail.getVerificationCode(email="hreem@eatinginseason.com", fromMail="cs@zepetto.id", start='OTP : <strong style="color: #000">', end='<')
print(mailbox)#N6Nhf6F1