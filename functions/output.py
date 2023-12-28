import os
from pyfiglet import figlet_format
from termcolor import cprint


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def banner():
    cprint(f"\n{figlet_format('Foxy Templates', font='elite')}",
           "yellow", "on_black")


def templates():
    folder_path = "./templates/"
    files = os.listdir(folder_path)
    files = [f for f in files if os.path.isfile(os.path.join(folder_path, f))]

    for i, file_name in enumerate(files, start=1):
        name, _ = os.path.splitext(file_name)
        neutral(f"{i}) {name}")


def neutral(text):
    cprint(f"{text}\n", "white", "on_black")


def error(text):
    print()
    cprint(f"[-]: {text}", "red", "on_black")
    print()
    exit(1)


def success(text):
    cprint(f"[+]: {text}", "green", "on_black")
