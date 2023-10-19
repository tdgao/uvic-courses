#!/usr/bin/env python3

import datetime

def main():
    """
    Florence is a nurse in a clinic. She is caring for 4 patients on
    different medication schedules

    * Mark needs medication every 5 hours
    * Susan needs medication every 3 hours
    * Chloe needs medication every 8 hours
    * Alexander needs medication every 10 hours

    Starting with your current day and time, make a care schedule
    for the next 14 days that Florence can use to schedule
    who needs medication at what time.

    Follow the steps provided.

    STEP 1: Use function patient_schedule to get a list of
    medication times for every patient
    """
    mark_schedule = patient_schedule("Mark", 5)
    susan_schedule = patient_schedule("Susan", 3)
    chloe_schedule = patient_schedule("Chloe", 8)
    alexander_schedule = patient_schedule("Alexander", 10)

    master_list = mark_schedule + susan_schedule + chloe_schedule + alexander_schedule
    master_list.sort()
    for item in master_list:
        formatted = item[0].strftime("%A, %d %m %Y, %X")
        print(formatted, item[1])
    
    """
    STEP 2: Combine all the lists and then form a master list of
    when medication is required by which patient.

    Print the medication schedule sorted by time in the format below:

      Friday, 25 03 2023, 09:24:27 Time to give medication to Alexander
      Friday, 25 03 2023, 10:24:27 Time to give medication to Chloe

    Refer to care_required.txt to see what the final output
    should look like. You are not required to write this information
    to a file. Simply output to console is enough.

    Note that care_required.txt does not contain the required output for
    this program. It only shows what the output should look like.

    HINT: You will need to keep track of who needs medication when.
    One way of doing this is with a dictionary. You may choose to
    use other ways.
    """
    # COMPLETE YOUR IMPLEMENTATION


def patient_schedule(patient_name, interval_in_hours):
    
    ''' This function will take a patient name and corresponding medication
     interval and return a list of tuples where each tuple contains the
     patient name and medication time in datetime object format)
    '''
    # COMPLETE YOUR IMPLEMENTATION
    list = []
    text = "Time to give medication to " + patient_name
    med_time = datetime.datetime.now()
    num_times = int( datetime.timedelta(days=14).total_seconds() / (interval_in_hours*60*60) )
    print( datetime.timedelta(days=14).seconds / (interval_in_hours*60*60) )

    for _ in range(num_times):
        med_time = med_time + datetime.timedelta(hours=interval_in_hours)
        list.append( (med_time,text) )
    return list

if __name__ == "__main__":
    main()