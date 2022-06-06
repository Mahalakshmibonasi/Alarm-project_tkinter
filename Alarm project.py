import datetime
from playsound import playsound
# from tkinter import*
# from tkinter.ttk import Combobox



hour=int(input("enter the hour:"))
minute=int(input("enter the minit:"))
AmPm=input(" am / pm : ")
ampm=AmPm.lower()

if ampm=="pm":
    hour+=12
elif ampm=="am":
    hour-=12

i=1
while i<=3:
    if (hour==datetime.datetime.now().hour and minute==datetime.datetime.now().minute):
        print(f"wake up it's {hour}:{minute}")
        playsound("/home/b/Downloads/Maha")
        i=i+1
print("good morning")



# #Importing all the necessary libraries to form the alarm clock:
# from tkinter import *
# import datetime
# import time
# import winsound

# def alarm(set_alarm_timer):
#     while True:
#         time.sleep(1)
#         current_time = datetime.datetime.now()
#         now = current_time.strftime("%H:%M:%S")
#         date = current_time.strftime("%d/%m/%Y")
#         print("The Set Date is:",date)
#         print(now)
#         if now == set_alarm_timer:
#             print("Time to Wake up")
#         winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
#         break
# def actual_time():
#     set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
#     alarm(set_alarm_timer)

# clock = Tk()
# clock.title("DataFlair Alarm Clock")
# clock.geometry("400x200")
# time_format=Label(clock, text= "Enter time in 24 hour format!", fg="red",bg="black",font="Arial").place(x=60,y=120)
# addTime = Label(clock,text = "Hour  Min   Sec",font=60).place(x = 110)
# setYourAlarm = Label(clock,text = "When to wake you up",fg="blue",relief = "solid",font=("Helevetica",7,"bold")).place(x=0, y=29)
# # The Variables we require to set the alarm(initialization):
# hour = StringVar()
# min = StringVar()
# sec = StringVar()
# #Time required to set the alarm clock:
# hourTime= Entry(clock,textvariable = hour,bg = "pink",width = 15).place(x=110,y=30)
# minTime= Entry(clock,textvariable = min,bg = "pink",width = 15).place(x=150,y=30)
# secTime = Entry(clock,textvariable = sec,bg = "pink",width = 15).place(x=200,y=30)
# #To take the time input by user:
# submit = Button(clock,text = "Set Alarm",fg="red",width = 10,command = actual_time).place(x =110,y=70)
# clock.mainloop()
# #Execution of the window.