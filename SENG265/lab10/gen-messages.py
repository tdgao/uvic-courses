#!/usr/bin/env python3

# usage: ./gen-message.py <csv-file-name>
import re
import datetime
import fileinput

template = """SUBSCRIPTION EXPIRY MESSAGE

==name==
==expired_date==


Dear ==name==:

Our records show that your subscription to "Unix Users Quarterly"
expired on ==expired_date==. 

If you would like to keep your subscription active, we request 
payment by December 31 2023.

Yours sincerely,

Uriah Heep"""


def main():
    today = datetime.date.today()
    six_weeks_from_today = today + datetime.timedelta(weeks=6)

    today = today.strftime("%B %d %Y")
    six_weeks_from_today = six_weeks_from_today.strftime("%B %d %Y")
    
    for line in fileinput.input():
        items = line.split(",")
        name = items[1] + " " + items[0]
        expired_date = items[2]
        filename = items[3]

        final = re.sub(r"==name==", name, template)
        final = re.sub(r"==expired_date==", expired_date, final)

        dirpath = "messages/%s" % (filename)     
        f = open("messages/%s.txt" % (filename), "w")
        f.write(final)
        f.close()
          
        pass


if __name__ == "__main__":
    main()