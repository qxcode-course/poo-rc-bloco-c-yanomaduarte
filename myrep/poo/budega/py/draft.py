class Person:
    def __init__(self, name: str):
        self.__name = name

    def getName(self) -> str:
        return self.__name

    def setName(self, name: str):
        self.__name = name

    def __str__(self):
        return self.__name


class Market:
    def __init__(self, qtd: int):
        self.__boxes = [None for i in range(qtd)]
        self.__queue = []

    def validateIndex(self, index: int) -> bool:
        return 0 <= index < len(self.__boxes)

    def __str__(self):
        boxes_str = "[" + ", ".join(
            c.getName() if c is not None else "-----" for c in self.__boxes
        ) + "]"
        queue_str = "[" + ", ".join(p.getName() for p in self.__queue) + "]"
        return f"Caixas: {boxes_str}\nEspera: {queue_str}"

    def arrive(self, person: Person):
        self.__queue.append(person)

    def call(self, index: int):
        if not self.validateIndex(index):
            print("fail: caixa inexistente")
            return
        if len(self.__queue) == 0:
            print("fail: sem clientes")
            return
        if self.__boxes[index] is not None:
            print("fail: caixa ocupado")
            return

        person = self.__queue[0]
        self.__queue = self.__queue[1:]
        self.__boxes[index] = person

    def finish(self, index: int):
        if not self.validateIndex(index):
            print("fail: caixa inexistente")
            return None
        if self.__boxes[index] is None:
            print("fail: caixa vazio")
            return None

        person = self.__boxes[index]
        self.__boxes[index] = None
        return person

    def cutInLine(self, person: Person, otherName: str):
        found = False
        new_queue = []
        for p in self.__queue:
            if p.getName() == otherName and not found:
                new_queue.append(person)
                found = True
            new_queue.append(p)
        if not found:
            new_queue.append(person)
        self.__queue = new_queue

    def giveUp(self, name: str):
        new_queue = []
        removed = False
        for p in self.__queue:
            if p.getName() == name and not removed:
                removed = True
                continue
            new_queue.append(p)
        if not removed:
            print("fail: cliente não encontrado")
        self.__queue = new_queue


def main():
    market = None

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
            qtd = int(args[1])
            market = Market(qtd)

        elif cmd == "show":
            print(market)

        elif cmd == "arrive":
            name = args[1]
            market.arrive(Person(name))

        elif cmd == "call":
            index = int(args[1])
            market.call(index)

        elif cmd == "finish":
            index = int(args[1])
            person = market.finish(index)

        elif cmd == "cut":
            name = args[1]
            otherName = args[2]
            market.cutInLine(Person(name), otherName)

        elif cmd == "giveup":
            name = args[1]
            market.giveUp(name)

        else:
            print("fail: comando inválido")


if __name__ == "__main__":
    main()
