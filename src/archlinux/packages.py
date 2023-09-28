from src.archlinux.arch import AUR
from src.run_command import run_command


def install_aur():
    run_command(f"sudo pacman -S --needed --noconfirm archlinux-keyring {AUR}")


def install_chaotic_aur():
    commands = ['sudo pacman-key --recv-key 3056513887B78AEB --keyserver keyserver.ubuntu.com',
        'sudo pacman-key --lsign-key 3056513887B78AEB',
        'sudo pacman -U \'https://cdn-mirror.chaotic.cx/chaotic-aur/chaotic-keyring.pkg.tar.zst\' \'https://cdn-mirror.chaotic.cx/chaotic-aur/chaotic-mirrorlist.pkg.tar.zst\'']
    for command in commands:
        run_command(command)

    with open('/etc/pacman.conf', 'a') as file:
        with open('files/chaotic_aur', 'r') as file2:
            file.write(file2.read())


def enable_fastest_mirror():
    run_command(f"{AUR} -S --needed --noconfirm reflector")
    run_command("sudo systemctl enable reflector.service")
    run_command("sudo reflector --latest 20 --protocol https --sort rate --fastest 10 --save /etc/pacman.d/mirrorlist")


def config_flatpak():
    run_command(f"{AUR} --needed --noconfirm flatpak")
    run_command("flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo")
