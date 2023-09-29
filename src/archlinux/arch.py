from src.archlinux.drivers import install_printer
from src.archlinux.gpu.amd import install_amd
from src.archlinux.gpu.intel import install_intel
from src.archlinux.gpu.nvidia import install_nvidia
from src.archlinux.packages import *
from src.archlinux.shell import *
from src.archlinux.system import *
from src.archlinux.tkg import install_kernel_tkg

AUR = "yay"


def arch_main(result):
    global AUR
    if not result["Gestionnaire d'AUR"]["yay"] and result["Gestionnaire d'AUR"]["paru"]:
        AUR = "paru"
    else:
        AUR = "yay"
    # Packages
    install_aur(AUR)
    install_chaotic_aur()
    enable_fastest_mirror(AUR)
    config_flatpak(AUR)

    # System
    setup_pacman()
    install_kernel_headers()
    setup_server_sound()
    setup_grub()
    setup_firewall()

    # Software
    install_lst('../lst/flatpak.lst', 'flatpak')
    install_lst('lst/packges.lst', AUR)

    # Shell
    if result["Shell"]["fish"]:
        install_shell(AUR, "fish")
    if result["Shell"]["zsh"]:
        install_shell(AUR, "zsh")

    # GPU
    if result["GPU"]["AMD"]:
        install_amd(AUR)
    if result["GPU"]["Intel"]:
        install_intel(AUR)
    if result["GPU"]["Nvidia"]:
        install_nvidia(AUR)

    install_printer(result["Imprimantes"]["Imprimantes non HP/EPSON"], result["Imprimantes"]["HP"],
                    result["Imprimantes"]["EPSON"])
    # Kernel
    install_kernel_tkg(AUR)
