"""
Time Slots:
Weekdays                    Weekends
0 -- 7:00 - 8:15 AM         10:15
1 -- 8:45 - 10:00 AM        12:00
2 -- 10:30 - 11:45 AM       2:00
3 -- 12:15 - 1:30 PM        3:45
4 -- 2:30 - 3:45 PM         5:30
5 -- 4:15 - 5:30 PM
6 -- 6:00 - 7:15 PM
7 -- 7:45 - 9:00 PM
"""

#Listed in order of priority for each day -- first is highest priority
SLOT_PREFERENCES = {
    'Mon': [0,1,2,3,4,5],
    'Tue': [0,1,2,3,4,5],
    'Wed': [0,1,2,3,4,5],
    'Thu': [0,1,2,3,4,5],
    'Fri': [0,1,2,3,4,5],
    'Sat': [0,1,2,3,4],
    'Sun': [0,1,2,3,4],
}