class Client:
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
        self.__seats: list[Client | None] = [None] * capacity

    def __verifyIndex(self, index: int):
        if 0 <= index < len(self.__seats):
            return True
        return False

    def __search(self, id: str) -> int:
        for i, client in enumerate(self.__seats):
            if client is not None and client.getId() == id:
                return i
        return -1

    def reserve(self, id: str, phone: int, index: int) -> bool:
        if not self.__verifyIndex(index):
            print(f"fail: cadeira nao existe")
            return False

        if self.__seats[index] is not None:
            print("fail: caideira ja esta ocupada")
            return False

        if self.__search(id) != -1:
            print(f"fail: cliente {id} ja esta no cinema")
            return False

        new_client = Client(id, phone)
        self.__seats[index] = new_client
        return True

    def cancel(self, id: str):
        index = self.__search(id)
        if index == -1:
            print(f"fail: cliente nao esta no cinema")
            return

        self.__seats[index] = None

    def getSeats(self) -> list[Client | None]:
        return self.__seats

    def toString(self):
        seat_strings = []
        for client in self.__seats:
            if client is None:
                seat_strings.append("-")
            else:
                seat_strings.append(str(client))

        return "[ " + " ".join(seat_strings) + " ]"

    def __str__(self) -> str:
        return self.toString()


def main():
    theater = None

    while True:
        line = input()
        print(f"${line}")
        args = line.split()

        if len(args) == 0:
            continue

        cmd = args[0]

        if cmd == "end":
            break

        elif cmd == "init":
            capacity = int(args[1])
            theater = Theater(capacity)

        elif cmd == "show":
            if theater:
                print(theater)

        elif cmd == "reserve":
            if theater:
                id = args[1]
                phone = int(args[2])
                index = int(args[3])
                theater.reserve(id, phone, index)

        elif cmd == "cancel":
            if theater:
                id = args[1]
                theater.cancel(id)


if __name__ == "__main__":
    main()
