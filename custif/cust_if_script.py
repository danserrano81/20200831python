#!/usr/bin/env python3
"""Author danserrano81 | Navy
	my first elif program"""
	
message = 'Your test is graded, you received '

# wrap connection in a float() to accept decimals as numbers
connection = input("What is your final score?")

if connection.isnumeric():
    connection = float(connection)
else:
    print("Please enter proper score")
    exit()

# if input value was higher or equal to 100
if connection >= 90:
    message = message + 'A - Amazing job'
elif connection >= 80:
    message = message + 'B - Great work'
elif connection >= 70:
    message = message + 'C - Average Joe'
elif connection >= 60:
    message = message + 'D - Almost failed'
elif connection <= 59:
    message = message + 'F - DO BETTER'		

print(message)
