import smtplib  
import datetime as dt  
import random  
  
# modify before git commit/pushing!!!  
my_email = "my_mail@gmail.com "  
target = "my_target_mail@gmail.com"  
password = "my_securepassword"  
  
now = dt.datetime.now()  
day_of_week = now.weekday()  
# date_of_birth = dt.datetime(year=1984, month=12, day=7)  
print(day_of_week)  
  
def random_quote_generator():  
    with open("quotes.txt") as citation:  
        quote_list = citation.readlines()  
    return random.choice(quote_list)  
  
  
  
if day_of_week == 0:  
    message = "Subject:Monday Motivational Quotes\n\n " + random_quote_generator()  
  
  
    with smtplib.SMTP("smtp.gmail.com") as connection:  
        connection.starttls()  
        connection.login(user=my_email, password=password)  
        connection.sendmail(  
            from_addr=my_email,  
            to_addrs=target,  
            msg=message  
        )

