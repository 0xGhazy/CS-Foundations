class Person:

    def __init__(self, name: str) -> None:
        self._name = name

    def _set_name(self, name: str) -> None:
        self._name = name

    def _get_name(self) -> str:
        return self._name

    name = property(_get_name, _set_name)

if __name__ == '__main__':
    x = Person("Hossam Hamdy")
    print(x.name)
    x.name = "Rooe@kali"
    print(x.name)
