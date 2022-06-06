class Student:

    def __init__(self, fname: str, lname: str) -> None:
        self.first_name = fname
        self.last_name = lname

    @property
    def fullname(self) -> str:
        return f"{self.first_name} {self.last_name}"

    @fullname.setter
    def fullname(self, name: str) -> None:
        self.first_name, self.last_name = name.split(" ")

    @fullname.deleter
    def fullname(self) -> None:
        print("My time has come!")

if __name__ == '__main__':
    s = Student("Hossam", "Hamdy")
    print(s.fullname)
    del s.fullname
    s.fullname = "Tony stark"
    print(s.fullname)
