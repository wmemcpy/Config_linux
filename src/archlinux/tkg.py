from src.run_command import run_command
from src.archlinux.arch import AUR


def install_kernel_tkg():
    run_command(f"{AUR} -S --needed --noconfirm linux-tkg-eevdf linux-tkg-eevdf-headers")
