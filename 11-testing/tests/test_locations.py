# ---------------------------------------------
#   Program by Anton B.
#
#   Ver.    Date
#   1.0     2021
# ---------------------------------------------
import unittest
from ..locations.location_function import get_city_country

class locations_testcase(unittest.TestCase):
    """Тесты для 'get_city_country'"""
    def test_city_country(self):
        """
        Строка вида 'Santiago, Chile'
        :return:
        """
        formatted_location = get_city_country('chile', 'santiago')
        self.assertEqual(formatted_location, 'Santiago, Chile')

def main():
    unittest.main()


if __name__ == '__main__':
    main()
