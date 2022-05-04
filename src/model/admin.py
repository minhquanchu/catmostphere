from model.user import User


class Admin(User):
    def __init__(self, username: str, password: str = None, dir: str = None) -> None:
        super().__init__(username, password, dir)

    def add(self) -> bool:
        pass

    def remove(self, username: str) -> bool:
        pass

    def get(self, username: str) -> User:
        pass

    def modify(self, user: User) -> bool:
        pass
