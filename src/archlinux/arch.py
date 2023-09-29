from src.archlinux.drivers import install_printer
from src.archlinux.gpu.amd import install_amd
from src.archlinux.gpu.intel import install_intel
from src.archlinux.gpu.nvidia import install_nvidia
from src.archlinux.packages import *
from src.archlinux.shell import *
from src.archlinux.system import *
from src.archlinux.tkg import install_kernel_tkg


def arch_main(result):
    if not result["Gestionnaire d'AUR"]["yay"] and result["Gestionnaire d'AUR"]["paru"]:
        aur: str = "paru"
    else:
        aur: str = "yay"

    # Packages
    install_chaotic_aur()
    enable_fastest_mirror(aur)
    install_aur(aur)
    config_flatpak(aur)

    # System
    setup_pacman()
    install_kernel_headers()
    setup_server_sound()
    setup_grub()
    setup_firewall()

    # Software
    install_lst('../lst/flatpak.lst', 'flatpak')
    install_lst('lst/packges.lst', aur)

    # Shell
    if result["Shell"]["fish"]:
        install_shell(aur, "fish")
    if result["Shell"]["zsh"]:
        install_shell(aur, "zsh")

    # GPU
    if result["GPU"]["AMD"]:
        install_amd(aur)
    if result["GPU"]["Intel"]:
        install_intel(aur)
    if result["GPU"]["Nvidia"]:
        install_nvidia(aur)

    install_printer(result["Imprimantes"]["Imprimantes non HP/EPSON"], result["Imprimantes"]["HP"],
                    result["Imprimantes"]["EPSON"])
    # Kernel
    install_kernel_tkg(aur)
