class Kid:
    def __init__(self, age: int, name: str):
        self.__age = age
        self.__name = name

    def getAge(self) -> int:
        return self.__age
    
    def getName(self) -> str:
        return self.__name

    def __str__(self) -> str:
        return {f"{self.__name}:{self.__age}"}

class Trampoline:
    def __init__(self):
        self.__waiting: list[Kid] = []
        self.__playing: list[Kid] = []

    def arrive(self, kid: Kid):
        slef.__waiting.append(kid)

    def enter(self):
        