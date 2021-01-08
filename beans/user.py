# FILL IN CODE
# Remove pass placeholder
class User:
    def __init__(self, user_id, user_name, mod=None, pref=None):
        self.__id = user_id
        self.__name = user_name

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def mod(self):
        return self.__mod

    @property
    def pref(self):
        return self.__pref

    @pref.setter
    def pref(self, value):
        self._pref = value

    @mod.setter
    def mod(self, value):
        self._mod = value