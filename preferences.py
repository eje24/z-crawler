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
PREFERENCES = {
    "Ben": {
        "username": "benjaminwu",
        "password": "f@JN#7-zxHaqhg",
        "SLOT_PREFERENCES": {
            'Mon': [7],
            'Tue': [],
            'Wed': [7],
            'Thu': [],
            'Fri': [7],
            'Sat': [],
            'Sun': [2, 3],
        }
    }, 
    "Albert": {
        "username": "axing",
        "password": "5Z9BY7A4f$bX7t",
        "SLOT_PREFERENCES": {
            'Mon': [7],
            'Tue': [],
            'Wed': [7],
            'Thu': [],
            'Fri': [7],
            'Sat': [],
            'Sun': [],
        }
    },
    "Ezra": {
        "username": "189823EErives",
        "password": "12345",
        "SLOT_PREFERENCES": {
            'Mon': [7],
            'Tue': [],
            'Wed': [7],
            'Thu': [],
            'Fri': [7],
            'Sat': [],
            'Sun': [],
        }
    },
    "Jerry": {
        "username": "JerryZhao16",
        "password": "benishot",
        "SLOT_PREFERENCES": {
            'Mon': [7],
            'Tue': [],
            'Wed': [7],
            'Thu': [],
            'Fri': [7],
            'Sat': [],
            'Sun': [],
        }
    }
}

"""
"Albert": {
        "username": "axing",
        "password": "5Z9BY7A4f$bX7t",
        "SLOT_PREFERENCES": {
            'Mon': [7],
            'Tue': [],
            'Wed': [7],
            'Thu': [],
            'Fri': [7],
            'Sat': [],
            'Sun': [],
        }
    },
    "Ezra": {
        "username": "189823EErives",
        "password": "12345",
        "SLOT_PREFERENCES": {
            'Mon': [7],
            'Tue': [],
            'Wed': [7],
            'Thu': [],
            'Fri': [7],
            'Sat': [],
            'Sun': [],
        }
    },
    "Jerry": {
        "username": "JerryZhao16",
        "password": "benishot",
        "SLOT_PREFERENCES": {
            'Mon': [7],
            'Tue': [],
            'Wed': [7],
            'Thu': [],
            'Fri': [7],
            'Sat': [],
            'Sun': [2, 3],
        }
    }
"""