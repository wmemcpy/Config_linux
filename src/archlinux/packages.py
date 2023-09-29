from src.run_command import run_command


def install_aur(aur: str):
    print("Installing de l'AUR")

    run_command(f"sudo pacman -S --needed --noconfirm archlinux-keyring {aur}")


def install_chaotic_aur():
    print("Installing Chaotic AUR")

    run_command("sudo pacman-key --recv-key 3056513887B78AEB --keyserver keyserver.ubuntu.com")
    run_command("sudo pacman-key --lsign-key 3056513887B78AEB")
    run_command("sudo pacman -U 'https://cdn-mirror.chaotic.cx/chaotic-aur/chaotic-keyring.pkg.tar.zst' 'https://cdn-mirror.chaotic.cx/chaotic-aur/chaotic-mirrorlist.pkg.tar.zst'")

    with open('/etc/pacman.conf', 'a') as file:
        with open('files/chaotic_aur', 'r') as file2:
            file.write(file2.read())


def enable_fastest_mirror(aur: str):
    print("Activation des mirroirs les plus rapides")

    run_command(f"{aur} -S --needed --noconfirm reflector")
    run_command("sudo systemctl enable reflector.service")
    run_command("sudo reflector --latest 20 --protocol https --sort rate --fastest 10 --save /etc/pacman.d/mirrorlist")


def config_flatpak(aur: str):
    print("Configuration de Flatpak")

    run_command(f"{aur} --needed --noconfirm flatpak")
    run_command("flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo")
