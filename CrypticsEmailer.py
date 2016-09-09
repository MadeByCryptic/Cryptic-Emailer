from guerrillamail import GuerrillaMailSession
from time import sleep
import smtplib
import random
import getpass

print "[*] Welcome To Cryptic's Fast & Simple Emailer"
sleep(1.5)
print "[*] Loading Script Now... "
sleep(2)
print "[*] Successfully Loaded!"
sleep(1)
print "[*] Choose One Of The Options Below:"
sleep(0.5)
print "\n [1]~Gmail\n [2]~Hotmail\n [3]~Yahoo\n [4]~ThrowAwayEmail\n [5]~Quit\n "
sleep(0.5)
option = raw_input("[*] Please Select An Option: ")
sleep(1)

if option == '1':

    MainLogin = raw_input("[*] Gmail: ")
    sleep(1)
    MainPassword = getpass.getpass(prompt="[*] Password: ")
    sleep(1)
    MainContact = raw_input("[*] Who Would You Like To Send The Email To: ")
    sleep(1)
    MainMessage = raw_input("[*] What Would You LIke The Email To Say: ")
    sleep(2)
    print "[*] Email Successfully Sent!"


    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(MainLogin, MainPassword)

    msg = (MainMessage)
    server.sendmail(MainLogin, MainContact, msg)
    server.quit()

elif option == '2':

    MainLogin = raw_input("[*] Hotmail: ")
    sleep(1)
    MainPassword = getpass.getpass(prompt="[*] Password: ")
    sleep(1)
    MainContact = raw_input("[*] Who Would You Like To Send The Email To: ")
    sleep(1)
    MainMessage = raw_input("[*] What Would You LIke The Email To Say: ")
    sleep(2)
    print "[*] Email Successfully Sent!"


    server = smtplib.SMTP('smtp.live.com', 587)
    server.starttls()
    server.login(MainLogin, MainPassword)

    msg = (MainMessage)
    server.sendmail(MainLogin, MainContact, msg)
    server.quit()

elif option == '3':

    MainLogin = raw_input("[*] Yahoo: ")
    sleep(1)
    MainPassword = getpass.getpass(prompt="[*] Password: ")
    sleep(1.5)
    MainContact = raw_input("[*] Who Would You Like To Send The Email To: ")
    sleep(1.5)
    MainMessage = raw_input("[*] What Would You LIke The Email To Say: ")
    sleep(2)
    print "[*] Email Successfully Sent!"


    server = smtplib.SMTP('smtp.mail.yahoo.com', 587)
    server.starttls()
    server.login(MainLogin, MainPassword)

    msg = (MainMessage)
    server.sendmail(MainLogin, MainContact, msg)
    server.quit()

elif option == '4':

    print "[*] Email Address Only Lasts For 60 Minutes."
    sleep(1)
    print "[*] Generating Email..."
    sleep(1.5)
    session = GuerrillaMailSession()
    print session.get_session_state()['email_address']

    print "[*] Enjoy Your ThrowAway Email!"

elif option == '5':
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.quit()
