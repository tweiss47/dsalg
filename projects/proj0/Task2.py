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
# * Lookup the longest time at the end since the overall runtime won't be
#   impacted and it is much simpler

number_map = {}
def update_durations(number_map, number, duration):
    last_duration = number_map.get(number, 0)
    number_map[number] = last_duration + duration

for source, dest, time, duration in calls:
    update_durations(number_map, source, int(duration))
    update_durations(number_map, dest, int(duration))

longest_number = max(number_map.keys(), key=(lambda k: number_map[k]))
longest = number_map[longest_number]

print(longest_number, "spent the longest time,", longest, "seconds, on the phone during September 2016.")

