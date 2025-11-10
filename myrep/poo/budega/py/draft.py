class Person:
    def __init__(self, name: str):
        self.__name = name

    def getName(self) -> str:
        return self.__name

    def setName(self, name: str):
        return self.__name

    def __str__(self):
        return self.__name


class Market:
    def __init__(self, name: str, counters: str):
        self.counter = [None for i in range(counters)]
        self.queue = []

    def validateIndex(self, index: int) -> bool:
        return 0 <= index < len(self.counters)

    def __str__(self):
        box_str = ", ".join(
            str(person) if person is not None else "-----"
            for person in self.__box
        )
        queue_str = ", ".join(str(person) for person in self.__queue)
        return f"Caixas: [{box_str}]\nEspera: [{queue_str}]"

    def arrive(self, person: Person):
        self.__queue.append(person)

    def call(self, index: int):
        if len(self.__queue) == 0:
            print("fail: não há clientes")
            return
        if self.__box[index] is not None:
            print("fail: caixa ocupado")
            return

    def finish(self, index: int):
        if not self.validateIndex(index):
            print("fail: caixa inexistente")
            return None
        if self.counters[index] is None:
            print("fail: caixa vazio")
            return None

        person = self.counters[index]
        self.counters[index] = None
        return person
