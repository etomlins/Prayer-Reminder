import schedule
from datetime import datetime
import time
import json 
import SMS


stop_loop=False

with open("test_novena.json", "r") as json_file:
    data = json.load(json_file)


def increment_counter():
    counter[0] += 1
    return None

def get_current_day():
    return counter[0]


def send_novena_message(json):
    day_number = str(get_current_day())
    print(day_number)
    for day, info in json.items():
        if day_number in day:
            print(day)
            subject = info[0]["Intention"]
            print(subject)
            body = info[0]["Prayer"]
            print(body)
            body = body.replace("\\n", "\n")
            break
        else:
            subject = "something wrong"
            body = "something wrong"
    SMS.send(subject,body)
    increment_counter()
    print("sent one novena message :)")
    print(get_current_day())

time_string = "12:35"

if __name__ == "__main__":
    
    counter = [1]
    time_interval_minutes = 1

# test every minute
    schedule.every(time_interval_minutes).minutes.do(
        send_novena_message, data)
# test every day
    schedule.every(1).day.at(time_string).do(send_novena_message,data)
    while not stop_loop:
        schedule.run_pending()
        time.sleep(1)
        if counter[0] >= 10:
            stop_loop=True
            goodbye_message_subj = "Final Message"
            goodbye_message_body = "This is the last message you'll receive. Congratulations on completing your novena. God bless!"
            SMS.send(goodbye_message_subj,goodbye_message_body)
            break


