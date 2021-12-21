# ---------------------------------------------
#   Program by Anton B.
#
#   Ver.    Date
#   1.0     2021
# ---------------------------------------------


def get_formatted_name(first, last, middle: str = '') -> str:
    """Строит отформатированное полное имя."""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()


def main():
    pass


if __name__ == '__main__':
    main()
