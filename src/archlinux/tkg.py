from src.run_command import run_command


def install_kernel_tkg(aur: str):
    run_command(f"{aur} -S --needed --noconfirm linux-tkg-eevdf linux-tkg-eevdf-headers")
