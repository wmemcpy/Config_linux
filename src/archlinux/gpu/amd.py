from src.install_lst import install_lst


def install_amd(aur: str):
    install_lst('lst/amd.lst', aur)
