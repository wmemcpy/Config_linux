from src.run_command import run_command
from src.archlinux.arch import AUR
from src.install_lst import install_lst


def install_printer(printer:bool = False, hp: bool = False, epson: bool = False):
    if printer or hp or epson:
        install_lst("lst/printer.lst", AUR)
    if hp:
        install_lst("lst/printer_hp.lst", AUR)
    if epson:
        install_lst("lst/printer_epson.lst", AUR)
