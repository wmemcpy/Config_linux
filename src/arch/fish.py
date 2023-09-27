import os
import subprocess
from pathlib import Path

from devices import read_user

def add_alias_u(file):
    alias_cmd = "alias update-arch='sudo pacman -Scc && sudo pacman -Syy && yay -S archlinux-keyring && yay && yay -Sc && sudo pacman -Rns $(pacman -Qdtq) && flatpak update'"
    try:
        if file.exists():
            with file.open() as f:
                content = f.read()
            if alias_cmd not in content:
                with file.open('a') as f:
                    f.write(f"{alias_cmd}\n")
        else:
            with file.open('w') as f:
                f.write(f"{alias_cmd}\n")
    except Exception as e:
        print(f"Erreur lors de l'ajout de l'alias : {e}")

def chose_shell():
    try:
        if 'fish' not in os.environ['SHELL']:
            if read_user("Voulez vous utiliser fish comme terminal ?"):
                subprocess.run(['sudo', 'pacman', '-S', '--noconfirm', 'fish', 'man-db', 'man-pages'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
                subprocess.run(['chsh', '-s', '/usr/bin/fish'], check=True)
                subprocess.run(['fish', '-c', 'fish_update_completions'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
                add_alias_u(Path(f"{os.environ['HOME']}/.config/fish/config.fish"))
                subprocess.run(['fish', '-c', 'set -U fish_greeting'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)

            else:
                add_alias_u(Path(f"{os.environ['HOME']}/.bashrc"))

    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de la configuration du shell : {e}")