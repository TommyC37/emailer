import smtplib
import datetime as dt
from decouple import config
import time

with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
  connection.ehlo()
  connection.starttls()

  from_addr = config('FROM_ADDR')
  from_password = config('FROM_PASS')

  to_addr = config('TO_ADDR')
  to_name = input('To name: ')
  subject = input('Subject: ')
  message = input('Message: ')
  from_name = input('From name: ')
  send_time = dt.datetime(2022,5,1,21,25,0,0)
  body = f"Subject:{subject}\n\nHi {to_name},\n\n{message}\n\nCheers,\n{from_name}"

  x=time.sleep(send_time.timestamp() - time.time())

  connection.login(user=from_addr, password=from_password)
  connection.sendmail(from_addr=from_addr, to_addrs=to_addr, msg=body)
