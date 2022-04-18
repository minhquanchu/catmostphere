from importlib.resources import path
import json
from typing import Tuple, Union


class User(dict):
    def __init__(self, username: str, password: str = None) -> None:
        self._path: str = None    
        self._username = username
        self._password = password
        self.name: str = None
        self._user: dict = {
            'name': self.name,
            'password': self._password
        }
        try:
            self._verified = self.verifier()
            self._registered = True
        except Exception:
            self._verified = False
            self._registered = False 

    @property
    def path(self) -> str:
        return self._path
    
    @path.setter
    def path(self, path: str) -> None:
        self._path = path

    def verifier(self, users: str, password: str = None) -> Union[bool, Tuple[bool, str]]:
        try:
            with open(f'{self.path}/{self.username}.json', 'r') as openFile:
                user = json.load(openFile)
                if password == user['pasword'] or self.password == user['password']:
                    return True
                return False
        except OSError:
            raise Exception(f'validation failed, username {self.username} does not exist')
    
    @property
    def username(self):
        return self._username
    
    @property
    def user(self) -> dict:
        return self._user

    def update(self) -> bool:
        try:
            with open(f'{self.path}/{self.username}.json', 'w') as openFile:
                json.dump(self.user, openFile, indent = 4, sort_keys = True)
                return True
        except OSError:
            raise Exception(f'update failed, username {self.username} does not exist')

