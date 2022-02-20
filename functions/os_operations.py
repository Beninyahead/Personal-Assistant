import os
import subprocess as sp

PATHS = {
    'notepad': "C:/Program Files (x86)/Notepad++/notepad++.exe",
    'calculator': "C:\\Windows\\System32\\calc.exe"
}

def open_camera():
    sp.run('start microsoft.windows,camera', shell=True)

def open_notepad():
    os.startfile(PATHS['notepad'])

def open_cmd():
    os.system('start cmd')

def open_calculator():
    sp.Popen(PATHS['calculator'])


if __name__ == '__main__':
    open_notepad()