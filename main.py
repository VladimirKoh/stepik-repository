print("Hellow world")


class Hellow_world:
    def __init__(self, name):
        self.name = name

    def get_name(self) -> str:
        print(self.name)

test = Hellow_world('Hello!')
test.get_name()