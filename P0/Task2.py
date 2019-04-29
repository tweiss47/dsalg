"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".
"""

# * All the phone calls are during September
# * Need to keep track of the caller and the callee time for each number
# * Need to keep track of the largest value and number. It is either the
#   current largest or one of the ones just updated
longest = 0
longest_number = ""
number_map = {}

def update_duration(number, duration):
    '''Update the number map and longest, longest_number for the current call.'''
    global longest, longest_number, number_map
    last_duration = number_map.get(number, 0)
    new_duration = last_duration + duration
    number_map[number] = new_duration
    if new_duration > longest:
        longest = new_duration
        longest_number = number

for source, dest, time, duration in calls:
    update_duration(source, int(duration))
    update_duration(dest, int(duration))

print(longest_number, "spent the longest time,", longest, "seconds, on the phone during September 2016.")

