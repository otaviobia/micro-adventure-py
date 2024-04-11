# Copyright (c) 2024 Otávio Biagioni
# License: MIT License
"""THE VAULT LOCK"""
import os
import time

day = 1
hour = 17
minute = 30
second = 0
increment = 1
interval = 0
week = "SUNDAY...MONDAY...TUESDAY..WEDNESDAYTHURSDAY.FRIDAY...SATURDAY"
if interval < 10:
	increment = 7
while hour != 8 and minute != 0 and second != 0 and day != 1:
	time.sleep(interval/10)
	os.system('clear')
	second = second + pow(increment, 2)
	if second >= 60:
		second = 0
		minute = minute + pow(increment, 2)
	if minute >= 60:
		minute = 0
		hour += 1
	if hour >= 24:
		hour = 0
		day += 1
	if day >= 7:
		day = 0
	print("THE VAULT IS CLOSED!\n")
	print("{:02d}:{:02d}:{:02d}\n".format(hour, minute, second))
	print(week[(day*9):(day*9)+9])
os.system('clear')
print("MONDAY 08:00 THE VAULT IS OPEN")