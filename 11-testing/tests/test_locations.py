# ---------------------------------------------
#   Program by Anton B.
#
#   Ver.    Date
#   1.0     2021
# ---------------------------------------------

import unittest
from ..locations.location_function import get_city_country


class LocationsTestCase(unittest.TestCase):
    """Тесты для 'get_city_country'"""
    
    def test_city_country(self):
        """Строка вида 'Santiago, Chile'"""
        formatted_location = get_city_country('chile', 'santiago')
        self.assertEqual(formatted_location,
                         'Santiago, Chile - population 5000000')
    
    def test_city_country_population(self):
        """Строка вида 'Santiago, Chile- population 5000000' """
        formatted_location = get_city_country('chile', 'santiago',
                                              population=5000000)
        self.assertEqual(formatted_location,
                         'Santiago, Chile - population 5000000')


def main():
    unittest.main()


if __name__ == '__main__':
    main()
