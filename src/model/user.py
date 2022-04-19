import json

from model.utils import getDBPath


class User(dict):
    def __init__(self, username: str, password: str = None) -> None:
        self._username = username
        self._dir: str = getDBPath() + f'/users/{self._username}.json'           
        self._password = password
        self._admin: bool = None
        self._name: str = None
        print('hello')
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

    def __str__(self):
        return f'This is the account of {self._username}'

    @property
    def verified(self) -> bool:
        return self._verified

    @property
    def dir(self) -> str:
        return self._dir
        
    
    @dir.setter
    def dir(self, dir: str) -> None:
        self._dir = dir
    
    @property
    def name(self) -> str:
        return self._name
        
    
    @name.setter
    def name(self, name: str) -> None:
        self._name = name
    
    @property
    def admin(self) -> bool:
        return self._admin

        
    @property
    def username(self):
        return self._username
    
    @property
    def user(self) -> dict:
        return self._user

    def verifier(self, password: str = None) -> bool:
        """
        verify user login to gain access <username>.json. The optional password is used to authorize access when you want to update user
        Exception is raised if user is not registered in the database (OSError)
        """
        try:
            with open(self.path, 'r') as openFile:
                user = json.load(openFile)
                if password == user['password']:
                    return True
                if self._password == user['password']:
                    self._name = user['name']
                    self._admin = user['admin']
                    return True
                return False
        except OSError:
            raise Exception(f'validation failed, username {self._username} does not exist')

    def update(self) -> bool:
        """
        Update user info to <username>.json
        """
        try:
            with open(f'{self.dir}/{self.username}.json', 'w') as openFile:
                json.dump(self.user, openFile, indent = 4, sort_keys = True)
                return True
        except OSError:
            raise Exception(f'update failed, username {self.username} does not exist')

     

