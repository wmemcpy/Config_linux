from src.install_lst import install_lst
from src.archlinux.arch import AUR

def install_kde():
    install_lst('../lst/kde.lst', AUR)