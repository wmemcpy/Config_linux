from os import rename, listdir, makedirs
from shutil import copyfile

from src.install_lst import install_lst
from src.run_command import run_command


def setup_pacman():
    uncomment: list[str] = ["#VerbosePkgLists", "#ParallelDownloads", "#Color"]
    pacman_src: str = "/etc/pacman.conf"

    with open(pacman_src, "r") as infile, open(pacman_src + ".tmp", "w") as outfile:
        for line in infile:
            if any(line.startswith(s) for s in uncomment):
                outfile.write(line[1:])
            else:
                outfile.write(line)

    rename(pacman_src + ".tmp", pacman_src)


def install_kernel_headers():
    kernels: list[str] = [f for f in listdir('/boot') if f.startswith('vmlinuz')]
    for kernel in kernels:
        run_command(f"sudo pacman -S --needed --noconfirm {kernel.replace('vmlinuz-', '')}-headers")


def setup_server_sound():
    remove_packages: list[str] = ["pulseaudio", "jack2", "pipewire-media-session", "pulseaudio-bluetooth",
        "pulseaudio-alsa"]
    for package in remove_packages:
        run_command(f"sudo pacman -Rdd --noconfirm {package}")

    install_lst("lst/server_sound.lst", "sudo pacman")


def setup_grub():
    grub_hook: str = "/etc/pacman.d/hooks/"

    makedirs(grub_hook, exist_ok=True)
    copyfile("files/grub.hook", grub_hook + "grub.hook")


def setup_firewall():
    run_command("sudo pacman -S --needed --noconfirm ufw")
    run_command("sudo systemctl enable ufw.service")
