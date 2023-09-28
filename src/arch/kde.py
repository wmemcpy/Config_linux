import subprocess

def install_kde():
    # install all packages in kde.lst
    try:
        with open('../kde.lst', 'r') as file:
            content = file.read()
            for package in content.splitlines():
                subprocess.run(['yay', '-S', '--needed', '--noconfirm', package], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception as e:
        print(f"Erreur lors de l'installation des paquets KDE : {e}")
