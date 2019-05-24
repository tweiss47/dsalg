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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

# Part A
#   loop through the calls
#   if the source is Bangalore
#       extract the prefix
#       add it to a set
#
# Part B
#   -- if we keep track of the count of the number of time called in Part A
#   then we can just compute Part B directly

def get_prefix_code(number):
    '''Extract the prefix from the phone number according to the rules above'''
    assert(len(number) > 1)
    if number[0] == '(':
        assert(number[1] == '0')
        return number[1:number.find(')')]
    elif number[0] == '1':
        assert(number[1] == '4' and number[2] == '0')
        return number[0:3]
    else:
        assert(number[0] == '7' or number[0] == '8' or number[0] == '9')
        return number[0:4]

calls_from_bangalore = 0
calls_to_bangalore = 0
dest_prefixes = set()
for source, dest, time, duration in calls:
    source_prefix = get_prefix_code(source)
    if source_prefix == '080':
        dest_prefix = get_prefix_code(dest)
        dest_prefixes.add(dest_prefix)
        calls_from_bangalore += 1
        if dest_prefix == '080':
            calls_to_bangalore += 1

print("The numbers called by people in Bangalore have codes:")
for prefix in sorted(dest_prefixes):
    print("", prefix)

percentage_within_bangalore = calls_to_bangalore / calls_from_bangalore * 100
print(percentage_within_bangalore, "percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")
