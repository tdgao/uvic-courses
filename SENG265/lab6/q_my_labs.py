#!/usr/bin/env python3

import datetime

def main():
    """
    Create a datetime object for today's date
    """

    # COMPLETE IMPLEMENTATION
    todays_date = datetime.date.today()

    date_list = every_lab(todays_date)
    for date in date_list:
        print( date.strftime("%a, %d %B %y"), sep='\n' )
    """ 
    variable date_list should contain datetime objects 
    for all the days when you have a lab
    print these dates in the format "Mon, 19 November 23"
    """

    # COMPLETE IMPLEMENTATION

    


def every_lab(todays_date: datetime.date):
    """
    Classes for the current semester end on Dec 4, 2023.

    Assume that you have a lab every week till the end of classes. 
    (Only your lab, in this instance.)

    This function will create datetimes objects for those labs, 
    add them to a list and then return this list
    """
    end = datetime.date(2023, 12, 4)
    date_list = []
    date = todays_date
    
    # loop through today until end of week
    for i in range(7):
        if (date.weekday() == 6): break
        
        if (date.weekday() == 3):
            date_list.append(date)
            break
        date = date + datetime.timedelta(days=1)
        
    num_weeks = int((end - date).days / 7)
    for i in range( num_weeks ):
        date = date + datetime.timedelta(days=7)
        date_list.append(date)

    return date_list


if __name__ == "__main__":
    main()