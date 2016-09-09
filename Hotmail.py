# email test (gmail)

from time import sleep
import smtplib
import random

print "[*] Welcome To Cryptic's Fast & Simple Emailer"
sleep(3)
print "[*] Loading Script Now... "
sleep(3)
print "[*] Successfully Loaded!"
sleep(1.5)
MainLogin = raw_input("[*] Hotmail: ")
sleep(1)
MainPassword = raw_input("[*] Password: ")
sleep(1.5)
MainContact = raw_input("[*] Who Would You Like To Send The Email To: ")
sleep(1.5)
MainMessage = raw_input("[*] What Would You LIke The Email To Say: ")
sleep(2)
print "[*] Email Successfully Sent!"


server = smtplib.SMTP('smtp.live.com', 587)
server.starttls()
server.login(MainLogin, MainPassword)

msg = (MainMessage)
server.sendmail(MainLogin, MainContact, msg)
server.quit()
