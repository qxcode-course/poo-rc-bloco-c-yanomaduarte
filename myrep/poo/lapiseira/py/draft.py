class Lead:
    def __init__(self, thickness: float, hardness: str, size: int):
        self.__thickness = thickness
        self.__hardness = hardness
        self.__size = size

    def getThickness(self) -> float:
        return self.__thickness

    def getHardness(self) -> str:
        return self.__hardness

    def getSize(self) -> int:
        return self.__size

    def setSize(self, size: int):
        self.__size = size

    def usagePerSheet(self) -> int:
        if self.__hardness == "HB":
            return 1
        elif self.__hardness == "2B":
            return 2
        elif self.__hardness == "4B":
            return 4
        elif self.__hardness == "6B":
            return 6
        return 0

    def __str__(self) -> str:
        return f"[{self.__thickness}:{self.__hardness}:{self.__size}]"


class Pencil:
    def __init__(self, thickness: float):
        self.__thickness = thickness
        self.__tip = None
        self.__barrel = []

    def insert(self, lead):
        if lead.getThickness() != self.__thickness:
            print("fail: calibre incompatível")
            return False
        self.__barrel.append(lead)
        return True

    def remove(self):
        if self.__tip is not None:
            lead_removed = self.__tip
            self.__tip = None
            return lead_removed
        return None

    def pull(self):
        if self.__tip is not None:
            print("fail: ja existe grafite no bico")
            return False

        if not self.__barrel:
            print("fail: tambor está vazio")
            return False

        pull_lead = self.__barrel[0]
        self.__tip = pull_lead
        self.__barrel = self.__barrel[1:]
        return True

    def writePage(self):
        if self.__tip is None:
            print("fail: nao existe grafite no bico")
            return

        current_size = self.__tip.getSize()
        if current_size <= 10:
            print("fail: tamanho insuficiente")
            self.remove()
            return

        wear = self.__tip.usagePerSheet()
        new_size = current_size - wear

        if new_size < 10:
            print("fail: folha incompleta")
            self.__tip.setSize(10)
            self.remove
        else:
            self.__tip.setSize(new_size)

    def show(self):
        tip_str = str(self.__tip) if self.__tip else "[]"
        barrel_str = "".join(str(lead) for lead in self.__barrel)
        print(
            f"calibre: {self.__thickness}, bico: {tip_str}, tambor: <{barrel_str}>")


def main():
    pencil = None

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
            pencil = Pencil(float(args[1]))

        elif cmd == "insert":
            thickness = float(args[1])
            hardness = args[2]
            size = int(args[3])
            lead = Lead(thickness, hardness, size)
            pencil.insert(lead)

        elif cmd == "pull":
            if pencil:
                pencil.pull()

        elif cmd == "remove":
            pencil.remove()

        elif cmd == "write":
            pencil.writePage()

        elif cmd == "show":
            pencil.show()


if __name__ == "__main__":
    main()
