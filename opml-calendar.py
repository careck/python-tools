# This script generates an OPML document for the months and days of the year
# it can be used to generate a template for any outliner application which can
# import OPML.
# This script was generated completely by ChatGPT given the following prompt:
# "Write a python program to print a hierarchical list of months and days for 2023 in OPML format"

import calendar

year = 2023

print("<?xml version='1.0' encoding='UTF-8'?>")
print("<opml version='1.0'>")
print("<head>")
print("<title>Calendar 2023</title>")
print("</head>")
print("<body>")

for month in range(1,13):
    print("  <outline text='"+calendar.month_name[month]+"'>")
    for day in range(1, calendar.monthrange(year, month)[1]+1):
        print("    <outline text='"+str(day)+" - "+calendar.day_name[calendar.weekday(year, month, day)]+"' />")
    print("  </outline>")

print("</body>")
print("</opml>")
