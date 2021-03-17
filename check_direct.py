def check_direct(DIRECTORY, dir):
    if DIRECTORY in dir:
        return True
    else:
        print('Вам разрешена работа только в рабочем каталоге!')
        return False