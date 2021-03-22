"""
Time Slots:
0 -- 7:00 - 8:15 AM
1 -- 8:45 - 10:00 AM
2 -- 10:30 - 11:45 AM
3 -- 12:15 - 1:30 PM
4 -- 2:30 - 3:45 PM
5 -- 4:15 - 5:30 PM
6 -- 6:00 - 7:15 PM
7 -- 7:45 - 9:00 PM
"""

#Listed in order of priority for each day -- first is highest priority
SLOT_PREFERENCES = {
    'Mon': [0,1,2],
    'Tues': [2,3],
    'Wed': [4,5],
    'Thurs': [5,6],
    'Fri': [1,4],
    'Sat': [5],
    'Sun': [5],
}