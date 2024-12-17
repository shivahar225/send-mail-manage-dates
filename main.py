import pandas
import smtplib
from datetime import datetime

my_email = "shivahar225@gmail.com"
password = "nfilawikdeheng"


today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    file_path = "letter_2.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("name",birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_person["email"],
            msg=f"subject:happy birthday\n\n{contents}"
        )
