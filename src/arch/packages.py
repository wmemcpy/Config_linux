import subprocess

def install_flatpak():
    try:
        subprocess.run(['sudo', 'pacman', '-S', '--needed', '--noconfirm', 'flatpak'], stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL)
        subprocess.run(
            ['flatpak', 'remote-add', '--if-not-exists', 'flathub', 'https://dl.flathub.org/repo/flathub.flatpakrepo'],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception as e:
        print(f"Erreur lors de l'installation de Flatpak : {e}")

def install_software():
    try:
        subprocess.run(['yay', '-S', '--needed', '--noconfirm', 'discord', 'visual-studio-code-bin'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.run(['flatpak', 'install', '-y', 'flathub', 'com.obsproject.Studio'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.run(['flatpak', 'install', '-y', 'flathub', 'com.valvesoftware.Steam'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.run(['flatpak', 'install', '-y', 'flathub', 'org.lutris.Lutris'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception as e:
        print(f"Erreur lors de l'installation des logiciels : {e}")

def install_flatpak():
    try:
        subprocess.run(['sudo', 'pacman', '-S', '--needed', '--noconfirm', 'flatpak'], stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL)
        subprocess.run(
            ['flatpak', 'remote-add', '--if-not-exists', 'flathub', 'https://dl.flathub.org/repo/flathub.flatpakrepo'],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception as e:
        print(f"Erreur lors de l'installation de Flatpak : {e}")


def install_useful_packages():
    try:
        subprocess.run(['yay', '-S', '--needed', '--noconfirm', 'fwupd', 'xdg-utils', 'reflector-simple', 'downgrade',
                        'rebuild-detector', 'mkinitcpio-firmware', 'xdg-desktop-portal', 'xdg-desktop-portal-gnome',
                        'neofetch', 'power-profiles-daemon', 'hunspell-fr', 'p7zip', 'unrar', 'ttf-liberation',
                        'noto-fonts-emoji-flags', 'ntfs-3g', 'fuse2', 'bash-completion', 'xdg-desktop-portal-gtk',
                        'ffmpegthumbs', 'vlc'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.run(['sudo', 'systemctl', 'enable', 'reflector.service'], stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL)

        result = subprocess.run(['lsblk', '-f'], stdout=subprocess.PIPE, text=True)
        if 'btrfs' in result.stdout:
            subprocess.run(['yay', '-S', '--needed', '--noconfirm', 'btrfs-progs', 'btrfs-assistant'],
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception as e:
        print(f"Erreur lors de l'installation des paquets utiles : {e}")

    install_flatpak()
