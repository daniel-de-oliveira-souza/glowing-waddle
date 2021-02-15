def checker(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('ERROR: Please, enter a valid number.')
            continue
        except KeyboardInterrupt:
            print('User would rather not to digit this number.')
            return 0
        else:
            return n


def line(size=42):
    return '-' * size


def header(txt):
    print(line())
    print(txt.center(42))
    print(line())


def menu(options):
    header('MAIN MENU')
    counter = 1
    for i in options:
        print(f'\033[33m{counter}\033[m - \033[34m{i}\033[m')
        counter += 1
    print(line())
    option = checker('\033[32mYour option: \033[m')
    return option