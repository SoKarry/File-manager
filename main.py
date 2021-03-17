import re
import os
import shutil
import shlex
import check_direct as chd


def crtdir(dir):
    os.mkdir(dir)

def rmvdir(dir):
    shutil.rmtree(dir)

def swapdir(dir):
    os.chdir(dir)

def crtfile(dir):
    open(dir, 'a').close()

def editfile(dir):
    edit_inp = input("Введите текст: ")
    with open(dir, "w") as file:
        file.write(edit_inp)

def readfile(dir):
    with open(dir, "r") as file:
        file_contents = file.read()
        print(file_contents)

def rmvfile(dir):
    os.remove(dir)

def cpyfile(dir1, dir2):
    shutil.copy2(dir1, dir2)

def movefile(dir1, dir2):
    shutil.move(dir1, dir2)

def renamefile(dir1, dir2):
    os.rename(dir1, dir2)

functions = {"crtdir":crtdir, "rmvdir":rmvdir, "swapdir":swapdir, "crtfile":crtfile, "editfile":editfile, "readfile":readfile, "rmvfile":rmvfile, "cpyfile":cpyfile, "movefile":movefile, "renamefile":renamefile}


with open('config.cfg', "r") as file:
    DIRECTORY = re.search(r'\"[^\"]*\"', file.read()).group().replace('"', '')
os.chdir(DIRECTORY)

while True:
    inp = input(f"@{os.getlogin()} {os.getcwd()}: ")
    spl_inp = shlex.split(inp)
    if spl_inp[0] in ["crtdir", "rmvdir", "swapdir", "crtfile", "editfile", "readfile", "rmvfile"]:
        abs_src_path = os.path.abspath(spl_inp[1])
        if chd.check_direct(DIRECTORY, abs_src_path):
            try:
                functions[spl_inp[0]](abs_src_path)
            except FileNotFoundError:
                print('Проверьте корректность введённого пути или названия файла :(')
    elif spl_inp[0] in ["cpyfile", "movefile", "renamefile"]:
        abs_src_path = os.path.abspath(spl_inp[1])
        abs_dst_path = os.path.abspath(spl_inp[2])
        if (chd.check_direct(DIRECTORY, abs_src_path) and chd.check_direct(DIRECTORY, abs_dst_path)):
            try:
                functions[spl_inp[0]](abs_src_path, abs_dst_path)
            except FileNotFoundError:
                print('Проверьте корректность введённого пути или названия файла :(')
    else:
        print('Такой команды не существует!')