import smtplib as s

ob = s.SMTP('smtp.gmail.com',587)
ob.ehlo()
ob.starttls()
ob.login('syedwahidali123456@gmail.com','xdxyfqfqqcmvecba')
subject="test python"
body="i love you sawa test"
message="subject:{}n\n{}".format(subject,body)
listadd=['abdul.wahidali.syed@gmail.com','syedwahidali215@gmail.com']
ob.sendmail('syedwahidali123456@gmail.com',listadd,message)
print("send email")