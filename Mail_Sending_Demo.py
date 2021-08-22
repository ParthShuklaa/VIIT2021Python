
import smtplib

MyConnection = smtplib.SMTP('smtp.gmail.com', 587)
MyConnection.starttls()
MyConnection.login("9ledgepro@gmail.com","Paasword")
MyMessage = "Hi There, Hope You are doing good, Start preparing for your Assessment"
MyConnection.sendmail("9ledgepro@gmail.com","parth.shukla@9ledgepro.com",MyMessage)
print("Mail Sent successfully, Check with receiver")
MyConnection.quit()

