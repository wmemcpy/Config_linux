import subprocess

def install_chaotic_aur():
    commands = [
        ['sudo', 'pacman-key', '--recv-key', '3056513887B78AEB', '--keyserver', 'keyserver.ubuntu.com'],
        ['sudo', 'pacman-key', '--lsign-key', '3056513887B78AEB'],
        ['sudo', 'pacman', '-U', 'https://cdn-mirror.chaotic.cx/chaotic-aur/chaotic-keyring.pkg.tar.zst', 'https://cdn-mirror.chaotic.cx/chaotic-aur/chaotic-mirrorlist.pkg.tar.zst'],
        ['sudo', 'bash', '-c', 'echo -e "[chaotic-aur]\nInclude = /etc/pacman.d/chaotic-mirrorlist" >> /etc/pacman.conf']
    ]
    for command in commands:
        subprocess.run(command)

    subprocess.run(['sudo', 'pacman', '-Syyu', '--noconfirm'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def install_kernel_tkg():
    try:
        subprocess.run(['yay', '-S', '--needed', '--noconfirm', 'linux-tkg-eevdf', 'linux-tkg-eevdf-headers'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception as e:
        print(f"Erreur : {e}")
