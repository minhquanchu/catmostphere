from datetime import datetime
from random import choice
from string import ascii_lowercase, ascii_uppercase


def rString(int: len = 8, lowercase: bool = True, uppercase: bool = True, digits: bool = True) -> bool:
    string = str('')
    for i in range(len):
        string += choice(f'{ascii_lowercase}{ascii_uppercase}{digits}')
    return string

def now() -> str:
    time = datetime.now().time()
    date = datetime.now().date()
    weekday = {
        0: 'mon',
        1: 'tue',
        2: 'wed',
        3: 'thu',
        4: 'fri',
        5: 'sat',
        6: 'sun'
    }
    return f'{time.hour}:{time.minute} {weekday[date.weekday()].capitalize()} {date.day}/{date.month}/{date.year}'
