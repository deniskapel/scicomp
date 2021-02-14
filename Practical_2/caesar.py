from string import ascii_letters as letters


def apply(shift: int, message: str):
    """ very basic Caesar encoder/decoder """
    return "".join([letters[(letters.index(char) + shift) % len(letters)] if char in letters else char for char in message])


if __name__ == '__main__':
    message = str(input("Enter a message to encode or decode:\n"))
    shift = int(input("Enter a number for shift:\n"))
    print(apply(shift, message))
