#!/usr/bin/env python3

import datetime as dt

LAB_DAY = 2
DAYS_IN_WEEK = 7

def every_lab(foo):
    print("This is outrageous! Unfair!")
    return None


def main():
    #Create a datetime object for today's date
    todays_date = dt.datetime.today()
    
    #contains datetime objects for all lab days
    date_list = every_lab(todays_date)

    #print lab dates in the format "Mon, 15 Jan 21"
    for date in date_list:
        date_str = date.strftime("%a, %d %b %y")
        print(date_str)

def every_lab(todays_date):
    """
    Assume that you have a lab every week till the end of classes. 
    (Only your lab, in this instance.)

    This function will create datetimes objects for those labs, 
    add them to a list and then return this list
    """
    last_day = dt.datetime(2024, 4, 8)
    date_list = []
    cur = todays_date
    
    #find the first day this week with a lab
    for day in range(1, DAYS_IN_WEEK+1):
        if cur.weekday() == LAB_DAY:
            break;
        cur = cur.replace(day = cur.day+1)
    
    #add all days which are lab days starting with the first day this week
    while cur <= last_day:
        date_list.append(cur)
        cur = cur + dt.timedelta(days = DAYS_IN_WEEK)
    
    return date_list


if __name__ == "__main__":
    main()
