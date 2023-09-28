import subprocess

def install_software():
    try:
        subprocess.run(['yay', '-S', '--needed', '--noconfirm', 'discord', 'visual-studio-code-bin', 'gdb', 'valgrind', 'clang'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        with open('../flatpak.lst', 'r') as file:
            content = file.read()
            for flatpak in content.splitlines():
                subprocess.run(['flatpak', 'install', 'flathub', '-y', flatpak], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

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
        with open('packages.lst', 'r') as file:
            content = file.read()
            for package in content.splitlines():
                subprocess.run(['yay', '-S', '--needed', '--noconfirm', package], stdout=subprocess.DEVNULL,
                               stderr=subprocess.DEVNULL)
        subprocess.run(['sudo', 'systemctl', 'enable', 'reflector.service'], stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL)

        result = subprocess.run(['lsblk', '-f'], stdout=subprocess.PIPE, text=True)
        if 'btrfs' in result.stdout:
            subprocess.run(['yay', '-S', '--needed', '--noconfirm', 'btrfs-progs', 'btrfs-assistant'],
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception as e:
        print(f"Erreur lors de l'installation des paquets utiles : {e}")

    install_flatpak()
