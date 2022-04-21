from datetime import datetime
from pathlib import Path
import platform
from random import choice
from string import ascii_lowercase, ascii_uppercase


def rString(int: len = 8, lowercase: bool = True, uppercase: bool = True, digits: bool = True) -> bool:
    """
    Return a random string of length len (len = 8 by default) containing upper/lowercase and digits
    """
    string = str('')
    for i in range(len):
        string += choice(f'{ascii_lowercase}{ascii_uppercase}{digits}')
    return string

def now() -> dict:
    """
    Return current time in dict format {'hour': int, 'minute': int, 'weekday': str, 'day': int, 'month': str, 'year': int}
    """
    time = datetime.now().time()
    date = datetime.now().date()
    weekdays = {
        0: 'mon',
        1: 'tue',
        2: 'wed',
        3: 'thu',
        4: 'fri',
        5: 'sat',
        6: 'sun'
    }
    months = {
        1: 'jan',
        2: 'feb',
        3: 'march',
        4: 'april',
        5: 'may',
        6: 'june',
        7: 'july',
        8: 'aug',
        9: 'dec',
        10: 'oct',
        11: 'nov',
        12: 'dec'
    }
    return {
        'hour': time.hour,
        'minute': time.minute,
        'weekday': weekdays[date.weekday()],
        'day': date.day,
        'month': months[date.month],
        'year': date.year
    }
def getDBPath(dir: str) -> str:
    """
    Return the absolute path <dir> in data
    """
    osName = platform.system()
    slash = ''
    if osName in ['Linux', 'Darwin']:
        slash = '/'
    elif osName == 'Windows':
        slash = '\\'
    dirPathList = str(Path.cwd()).split(f'{slash}')
    projectIndex = dirPathList.index('catmostphere') + 1
    absPath = f'{slash}'.join(dirPathList[0:projectIndex])
    return f'{absPath}{slash}data{slash}{dir}{slash}'





