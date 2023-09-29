from pathlib import Path

from src.run_command import run_command


def add_alias(aur: str, file=Path.home() / ".bashrc"):
    if aur == "paru":
        alias = "alias u='paru -Syy --needed archlinux-keyring && paru -c && flatpak update -y'"
    else:
        alias = "alias u='sudo pacman -Syy && yay -S archlinux-keyring && yay && yay -Sc && sudo pacman -Rns $(pacman -Qdtq) && flatpak update -y'"

    with open(file, "a") as f:
        if alias not in f.read():
            f.write(f"\n{alias}\n")
            print(f"Alias added to {file}")


def install_shell(aur: str, shell: str = "bash"):
    run_command(f"{aur} -S --needed --noconfirm {shell}")
    if shell == "zsh":
        add_alias(aur, Path.home() / ".zshrc")
    elif shell == "fish":
        add_alias(aur, Path.home() / ".config/fish/config.fish")
        run_command("fish -c 'fish_update_completions && set -U fish_greeting'")
    else:
        add_alias()

    run_command(f"chsh -s $(which {shell})")
