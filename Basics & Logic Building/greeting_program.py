# This program takes time input (hours, minutes, seconds) from the user,
# converts it into total seconds, and displays an appropriate greeting
# (Good Morning, Afternoon, or Evening) based on the time


hh = int(input("Enter the hour in 24- hour format:"))
mm = int(input("Enter the minutes in 60-minutes format:"))
ss = int(input("Enter the seconds in 60-seconds format:"))
time = hh*3600 + mm*60 +ss
print("Time in seconds:",time)
if(time<43200):
  print("Good Morning Mam/Sir")
elif(time>=43200 and time<64800):
  print("Good Afternoon Mam/Sir")
else:
  print("Good Evening Mam/Sir")
