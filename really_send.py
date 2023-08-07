# ------------RUN THIS FILE TO REALLY SEND THE MESSAGES------------
# need to run "nohup python3 really_send.py &"" in terminal
# to run code in the background. To check the output and see
# if there's any errors, run "tail -f nohup.out"

import schedule
from datetime import datetime
import time
import json 
import SMS

stop_loop=False

with open("novena.json", "r") as json_file:
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
    print(f"now it is day {get_current_day()}")

# send at 9am every day (based on time of computer this is run on)
time_string = "09:00"

if __name__ == "__main__":
    
    print("Starting automated Novena messages now. Happy praying!")
    # initialize counter that will increment every day
    counter = [1]
    
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


