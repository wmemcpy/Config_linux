from main import result
from src.archlinux.gpu.amd import install_amd
from src.archlinux.gpu.intel import install_intel
from src.archlinux.gpu.nvidia import install_nvidia
from src.archlinux.packages import *
from src.archlinux.shell import *
from src.archlinux.system import *
from src.archlinux.tkg import install_kernel_tkg

if not result["Gestionnaire d'AUR"]["yay"] and result["Gestionnaire d'AUR"]["paru"]:
    AUR = "paru"
else:
    AUR = "yay"


def main():
    # Packages
    install_aur()
    install_chaotic_aur()
    enable_fastest_mirror()
    config_flatpak()

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
        install_shell("fish")
    if result["Shell"]["zsh"]:
        install_shell("zsh")

    # GPU
    if result["GPU"]["AMD"]:
        install_amd()
    if result["GPU"]["Intel"]:
        install_intel()
    if result["GPU"]["Nvidia"]:
        install_nvidia()

    install_kernel_tkg()
