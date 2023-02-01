from sys import argv

from BruteForceDictionary import BruteForceDictionary
from BruteForceOptional import BruteForceOptional
from PasswordSender import PasswordSender

option = argv[1]
address = argv[2]
username = argv[3]


if __name__ == '__main__':
    brute = []
    sender = PasswordSender(address, username)
    correct = False

    if option[0] == 'd':
        brute = BruteForceDictionary()
    elif option[0] == 'o':
        length = argv[4]
        characters = argv[5]
        try:
            length = int(argv[4])
            characters = argv[5]
        except Exception:
            raise Exception("Неверный ввод: отсутствуют параметры длины и набора символов")
        brute = BruteForceOptional(characters, length)

    password = brute.get_password()
    while password != "":
        if sender.send_password(password):
            print("\nПароль для пользователя {0} найден: {1}".format(username, password))
            correct = True
            break
        else:
            password = brute.get_password()

    if not correct:
        print("\nПароль для пользователя {0} не был найден".format(username))

