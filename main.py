import datetime
import time

import yagmail
import pandas
from news import NewsFeed

while True:
    if datetime.datetime.now().hour == 15 and datetime.datetime.now().minute == 55:
        try:
            df = pandas.read_excel('people.xlsx')
        except Exception as e:
            print(f"Failed to read Excel file: {e}")
            exit()

        for index, row in df.iterrows():
            today = datetime.datetime.now().strftime('%y-%m-%d')
            yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%y-%m-%d')
            news_feed = NewsFeed(interest=row['interest'],
                                 from_date=yesterday,
                                 to_date=today)



            # Set up the SMTP client
            try:
                email = yagmail.SMTP(user="", password="k")
            except Exception as e:
                print(f"Failed to set up SMTP client: {e}")
                continue  # Skip to the next iteration if SMTP setup fails

            # Send the email
            try:
                email.send(
                    to=row['email'],
                    subject=f"Your {row['interest']} news for today",
                    contents=f"Hi {row['name']},\n\nSee what's on about {row['interest']} today:\n\n{news_feed.get()}"
                )
                print("Email sent successfully.")
            except Exception as e:
                print(f"Failed to send email: {e}")

            # Close the SMTP connection
            try:
                email.close()
            except Exception as e:
                print(f"Failed to close SMTP connection: {e}")

    time.sleep(60)
