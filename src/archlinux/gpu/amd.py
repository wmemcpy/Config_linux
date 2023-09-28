from src.archlinux.arch import AUR
from src.install_lst import install_lst


def install_amd():
    install_lst('lst/amd.lst', AUR)
