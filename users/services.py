import json


class UserService:
    __file_name = 'user_db.json'
    __users = []

    @classmethod
    def _read(cls) -> None:
        try:
            with open(cls.__file_name) as file:
                cls.__users = json.load(file)
        except (Exception,):
            pass

    @classmethod
    def _write(cls) -> None:
        with open(cls.__file_name, 'w') as file:
            json.dump(cls.__users, file)

    @classmethod
    def get_all(cls) -> list:
        return cls.__users

    @classmethod
    def get_by_id(cls, pk: int) -> dict:
        return next((item for item in cls.__users if item['id'] == pk), 'User not found')

    @classmethod
    def add(cls, data: dict) -> dict:
        user_id = cls.__users[-1]['id'] + 1 if len(cls.__users) else 1
        new_user = {**data, 'id': user_id}
        cls.__users.append(new_user)
        cls._write()
        return new_user

    @classmethod
    def update_by_id(cls, pk: int, data: dict) -> dict | str:
        user: dict = cls.get_by_id(pk)

        if isinstance(user, str):
            return user

        user.clear()
        user |= {**data, 'id': pk}
        cls._write()
        return user

    @classmethod
    def deleted_by_id(cls, pk: int) -> str:
        index = next((i for i, item in enumerate(cls.__users) if item['id'] == pk), 'User not found')

        if isinstance(index, str):
            return index

        del cls.__users[index]
        cls._write()
        return 'deleted'
