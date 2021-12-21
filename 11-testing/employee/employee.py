# ---------------------------------------------
#   Program by Anton B.
#
#   Ver.    Date
#   1.0     2021
# ---------------------------------------------

class Employee:
    """
    Работник
    :arg
        name(str): Name
        surname(str): Surname
        salary(int): Salary
    :argument
        name(str): Name
        surname(str): Surname
        salary(int): Salary
    """
    
    def __init__(self, name: str, surname: str, salary: int) -> None:
        self.name = name
        self.surname = surname
        self.salary = salary
    
    def give_raise(self, addsalary: int = 5_000) -> None:
        self.salary += addsalary
