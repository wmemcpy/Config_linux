import subprocess
import os

def gamepad():
    subprocess.run(['yay', '-S', '--needed', '--noconfirm', 'xpadneo-dkms'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def epson_printer():
    try:
        subprocess.run(
            ['yay', '-S', '--needed', '--noconfirm', 'epson-inkjet-printer-escpr', 'epson-inkjet-printer-escpr2',
             'epson-inkjet-printer-201601w', 'epson-inkjet-printer-n10-nx127'], stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL)
    except Exception as e:
        print(f"Erreur : {e}")

def hp_printer():
    try:
        subprocess.run(['yay', '-S', '--needed', '--noconfirm', 'hplip', 'python-pyqt5'], stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL)
    except Exception as e:
        print(f"Erreur : {e}")

def printer():
    subprocess.run(
            ['yay', '-S', '--needed', '--noconfirm', 'ghostscript', 'gsfonts', 'cups', 'cups-filters', 'cups-pdf',
             'system-config-printer', 'avahi', 'foomatic-db-engine', 'foomatic-db', 'foomatic-db-ppds',
             'foomatic-db-nonfree', 'foomatic-db-nonfree-ppds', 'gutenprint', 'foomatic-db-gutenprint-ppds'],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    subprocess.run(['sudo', 'systemctl', 'enable', '--now', 'avahi-daemon'], stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL)
    subprocess.run(['sudo', 'systemctl', 'enable', '--now', 'cups'], stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL)


def enable_bluetooth():
    try:
        subprocess.run(['sudo', 'pacman', '-S', '--needed', '--noconfirm', 'bluez-hciconfig'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception as e:
        print(f"Erreur : {e}")

    if os.system("hciconfig -a") == 0:
        subprocess.run(['yay', '-S', '--needed', '--noconfirm', 'bluez', 'bluez-utils', 'bluez-plugins'],
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.run(['sudo', 'systemctl', 'enable', '--now', 'bluetooth'], stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL)
    else:
        print("Bluetooth n'est pas supporté sur cet ordinateur.")

    try:
        subprocess.run(['sudo', 'pacman', '-R', '--noconfirm', 'bluez-hciconfig'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception as e:
        print(f"Erreur : {e}")



# Appeler les fonctions
gamepad()
printer()
enable_bluetooth()
