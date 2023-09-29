from pathlib import Path

from src.install_lst import install_lst
from src.archlinux.arch import AUR

def shortcut():
    config_file = open(Path.home() / ".config/i3/config", "a")

    with open("../../config/i3", "r") as f:
        config_file.write(f.read())

    config_file.close()

def install_i3():
    install_lst("../lst/i3.lst", AUR)
