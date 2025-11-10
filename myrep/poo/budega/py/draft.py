class Person:
    def __init__(self, name: str):
        self.__name = name

    def getName(self) -> str:
        return self.__name

    def setName(self, name: str):
        return self.__name

    def __str__(self):
        return f"{self.__name}"

class Market:
    def __init__(self, name: str, counters: str):
        self.__name = name
        self.counters = [None] * qtd_counters

    self.waiting = []

    