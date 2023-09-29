from src.install_lst import install_lst


def install_printer(aur: str, printer: bool = False, hp: bool = False, epson: bool = False):
    if printer or hp or epson:
        install_lst("lst/printer.lst", aur)
    if hp:
        install_lst("lst/printer_hp.lst", aur)
    if epson:
        install_lst("lst/printer_epson.lst", aur)
