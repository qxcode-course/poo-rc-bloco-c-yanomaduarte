class Cliente:
    def __init__(self, id: str, phone: int):
        self.__id = id
        self.__phone = phone

    def getPhone(self) -> int:
        return self.__phone

    def setPhone(self, phone: int):
        self.__phone = phone

    def getId(self) -> str:
        return self.__id

    def setId(self, id: str):
        self.__id = id

    def __str__(self) -> str:
        return f"[{self.__id}:{self.__phone}]"


class Theater:
    def __init__(self, capacity: int):
        self.__capacity = capacity


def main():
    theater = Theater()

    while True:
        line = input()
        print(f"${line}")
        args = line.split()

        if len(args) == 0:
            continue

        cmd = args[0]

        if cmd == "end":
            break
