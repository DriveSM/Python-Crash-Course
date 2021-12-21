# ---------------------------------------------
#   Program by Anton B.
#
#   Ver.    Date
#   1.0     2021
# ---------------------------------------------
import unittest
from ..employee.employee import Employee


class EmployeeTestCase(unittest.TestCase):
    """Тесты для класса Employee"""
    
    def setUp(self):
        """Создание работника для всех тестовых методов."""
        self.my_employee = Employee(name='Bob', surname='Brown', salary=10_000)
        self.clear_salary = self.my_employee.salary
    
    def test_give_default_raise(self):
        """Проверяет что прибавка к зарплате равна стандартной"""
        self.my_employee.give_raise()
        self.assertEqual(self.my_employee.salary, self.clear_salary + 5000)
    
    def test_give_custom_raise(self):
        """Проверяет что прибавка к зарплате равна введенной"""
        self.my_employee.give_raise(addsalary=7000)
        self.assertEqual(self.my_employee.salary, self.clear_salary + 7000)


def main():
    unittest.main()


if __name__ == '__main__':
    main()
