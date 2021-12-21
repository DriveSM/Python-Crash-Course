# ---------------------------------------------
#   Program by Anton B.
#
#   Ver.    Date
#   1.0     2021
# ---------------------------------------------

def get_city_country(country: str, city: str, population: int = 5_000_000) -> str:
    """
    Форматированная строка вида "Город, Страна"
    :param country: (str) country
    :param city: (str) city
    :return: (str) "City, Country"
    """
    string_line = f'{city.title()}, {country.title()} - population {population}'
    return string_line


def main():
    pass


if __name__ == '__main__':
    main()
