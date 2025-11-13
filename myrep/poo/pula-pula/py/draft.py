class Kid:
    def __init__(self, name: str, age: int):
        self.__name = name
        self.__age = age

    def getName(self) -> str:
        return self.__name

    def getAge(self) -> int:
        return self.__age

    def setName(self, name: str):
        self.__name = name

    def setAge(self, age: int):
        self.__age = age

    def __str__(self) -> str:
        return f"{self.__name}:{self.__age}"


class Trampoline:
    def __init__(self):
        self.__waiting: list[Kid] = []
        self.__playing: list[Kid] = []

    def arrive(self, kid: Kid):
        self.__waiting.append(kid)

    def enter(self):
        if not self.__waiting:
            print("fail: fila de espera vazia")
            return

        kid_enter = self.__waiting[0]
        self.__waiting = self.__waiting[1:]

        self.__playing.append(kid_enter)

    def leave(self):
        if not self.__playing:
            return None

        kid_leave = self.__playing[0]
        self.__playing = self.__playing[1:]

        self.__waiting.append(kid_leave)

    def removeFromList(self, name: str, kid_list: list[Kid]) -> Kid | None:
        for i, kid in enumerate(kid_list):
            if kid.getName() == name:
                del kid_list[i]
                return kid
        return None

    def removeKid(self, name: str) -> Kid | None:
        kid_removed = self.removeFromList(name, self.__waiting)
        if kid_removed:
            return kid_removed

        kid_removed = self.removeFromList(name, self.__playing)
        if kid_removed:
            return kid_removed

        print(f"fail: {name} nao esta no pula-pula")
        return None

    def toString(self) -> str:
        wait_str = ", ".join(str(kid) for kid in self.__waiting[::-1])
        play_str = ", ".join(str(kid) for kid in self.__playing[::-1])
        return f"[{wait_str}] => [{play_str}]"


def main():
    trampoline = Trampoline()

    while True:
        line = input()
        print(f"${line}")
        args = line.split()

        cmd = args[0]

        if cmd == "end":
            break

        elif cmd == "show":
            print(trampoline.toString())

        elif cmd == "arrive":
            name = args[1]
            age = int(args[2])
            kid = Kid(name, age)
            trampoline.arrive(kid)

        elif cmd == "enter":
            trampoline.enter()

        elif cmd == "leave":
            trampoline.leave()

        elif cmd == "remove":
            name = args[1]
            trampoline.removeKid(name)


if __name__ == "__main__":
    main()
