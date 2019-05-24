"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

#   build a set of everyone who texts or receives calls
#   for each number making a call:
#       if it is not in the set of non marketers
#           add it to the marketers set
#
#   Could do this with set operations
#       marketers = callers - receivers union texters

callers = set()
receivers = set()
texters = set()

for source, dest, time in texts:
    texters.add(source)
    texters.add(dest)

for source, dest, time, duration in calls:
    callers.add(source)
    receivers.add(dest)

marketers = callers - (texters | receivers)
print("These numbers could be telemarketers:")
for number in sorted(marketers):
    print(number)
