class User:
    def __init__(self, user_id, user_name, user_username):
        self.__id = user_id
        self.__name = user_name
        self.__username = user_username

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def username(self):
        return self.__username