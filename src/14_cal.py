"""
The Python standard library's 'calendar' module allows you to 
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `calendar.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should 
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that 
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
from calendar import TextCalendar
from datetime import datetime

cal = TextCalendar()

UsageError = Exception("""
  Please provide a month and then year, as numbers, e.g. python3 14_cal.py 5 2019
  Or provide nothing at all to get the current month's calendar.
  """)

try:
    if len(sys.argv) == 1:
        query_month = datetime.today().month
        query_year = datetime.today().year
    elif len(sys.argv) == 2:
        query_month = int(sys.argv[1])
        query_year = datetime.today().year
    elif len(sys.argv) == 3:
        query_month = int(sys.argv[1])
        query_year = int(sys.argv[2])
    else:
        raise UsageError

    cal.prmonth(query_year, query_month)

except:
    print(UsageError)


# let proper_usage = Exception('Text ')

# def globalist_month():
#   global query_month
#   try:
#     query_month = int(sys.argv[1])
#   except:
#   finally:
#     query_month = datetime.today().month

# def globalist_year():
#   global query_year
#   try:
#     query_year = int(sys.argv[2])
#   except:
#     query_year = datetime.today().year


# globalist_month()
# globalist_year()

# print(cal.prmonth(query_year, query_month))
