from tkinter import *
import datetime
import time
import winsound


def alarm(set_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()

        time_now = current_time.strftime("%H:%M:%S")
        date_now = current_time.strftime("%d/%m/%Y")

        print("Current date and current time is: " + date_now + " - " + time_now)

        if time_now == set_timer:
            print("Time to wake up!")
            winsound.PlaySound("HornAlarm.wav", winsound.SND_LOOP + winsound.SND_ASYNC)
            break


def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)


clock = Tk()

clock.title("Alex's custom clock alarm")
clock.geometry("310x150")

time_format = Label(clock, text="Enter time in 24h format!", fg="black", bg="white", font="Arial").place(x=0, y=200)
addTime = Label(clock, text="Hour  Minute   Second", font=200).place(x=0)
setYourAlarm = Label(clock, text="Time to wake up", fg="black", font=("Arial", 15, "bold")).place(x=0, y=50)

hour = StringVar()
min = StringVar()
sec = StringVar()

hourTime = Entry(clock, textvariable=hour, bg="white", width=15).place(x=0, y=30)
minTime = Entry(clock, textvariable=min, bg="white", width=15).place(x=40, y=30)
secTime = Entry(clock, textvariable=sec, bg="white", width=11).place(x=95, y=30)

submit = Button(clock, text="Set the Alarm", fg="black", bg="white", width=20, command=actual_time).place(x=20, y=90)

clock.mainloop()



