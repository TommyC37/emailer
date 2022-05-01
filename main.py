import smtplib
from decouple import config

with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
  connection.starttls()

  from_addr = config('FROM_ADDR')
  from_password = config('FROM_PASS')

  to_addr = config('TO_ADDR')
  subject = 'I just sent this email from Python!'
  body = f"Subject:{subject}\n\n\HeyTom,\n\nHow crazy is this?\n\n\I wonder if I can use this strange new power to build an email automation software for salespeople (that doesn't suck).\n\n\-Tom"

  connection.login(user=from_addr, password=from_password)
  connection.sendmail(from_addr=from_addr, to_addrs=to_addr, msg=body)
