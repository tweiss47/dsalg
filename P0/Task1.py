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
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
"""
numbers = set()
for source, dest, time in texts:
    numbers.add(source)
    numbers.add(dest)

for source, dest, time, duration in calls:
    numbers.add(source)
    numbers.add(dest)

print("There are", len(numbers), "different telephone numbers in the records.")

