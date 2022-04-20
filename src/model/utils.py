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

def now() -> str:
    """
    Return current time in string format (e.g 11:23 1/4/2022)
    """
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





