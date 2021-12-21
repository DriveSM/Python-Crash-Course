# ---------------------------------------------
#   Program by Anton B.
#
#   Ver.    Date
#   1.0     2021
# ---------------------------------------------
import unittest
from ..name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """Тесты для 'name_function.py'."""
    
    def test_first_last_name(self):
        """Имена вида 'Janis Joplin' работают правильно?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_name2(self):
        """Имена вида 'Janis Lyn Joplin' работают правильно?"""
        formatted_name = get_formatted_name('janis lyn', 'joplin')
        self.assertEqual(formatted_name, 'Janis Lyn Joplin')


def main():
    unittest.main()


if __name__ == '__main__':
    main()
