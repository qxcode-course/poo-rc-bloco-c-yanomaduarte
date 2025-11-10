class Person:
    def __init__(self, name: str):
        self.__name = name

    def getName(self) -> str:
        return self.__name

    def setName(self, name: str):
        return self.__name

    def __str__(self):
        return self.__name