import os
import shutil
import re
import subprocess


def hook():
    hook_folder = "/etc/pacman.d/hooks/"
    hook_file = "nvidia.hook"
    hook_src = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../../data/nvidia.hook")

    try:
        shutil.copy(hook_src, os.path.join(hook_folder, hook_file))
    except Exception as e:
        print(f"Erreur lors de la copie du hook : {e}")


def mkinitcpio():

    mkinitcpio_src = "/etc/mkinitcpio.conf"

    try:
        with open(mkinitcpio_src, 'r') as file:
            content = file.read()

        content = re.sub(r'(MODULES=.*\))', r'\1 nvidia nvidia_modeset nvidia_uvm nvidia_drm', content)

        with open(mkinitcpio_src, 'w') as file:
            file.write(content)
    except Exception as e:
        print(f"Erreur lors de la configuration de mkinitcpio : {e}")


def bootloaders():
    if os.path.isdir("/boot/loader/entries"):
        boot_loader = "systemd-boot"
    else:
        boot_loader = "grub"

    try:
        if boot_loader == "grub":
            boot_loader_src = "/etc/default/grub"

            with open(boot_loader_src, 'r') as file:
                content = file.read()

            if "GRUB_CMDLINE_LINUX_DEFAULT" in content and "nvidia-drm.modeset=1" not in content:
                content = re.sub(r'(GRUB_CMDLINE_LINUX_DEFAULT=".*?")', r'\1 nvidia-drm.modeset=1"', content)

                with open(boot_loader_src, 'w') as file:
                    file.write(content)

            subprocess.run(['sudo', 'grub-mkconfig', '-o', '/boot/grub/grub.cfg'], stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL)
        else:
            boot_loader_src = "/boot/loader/entries/*.conf"

            subprocess.run(['sudo', 'sed', '-i', '/^options root/ s/$/ nvidia-drm.modeset=1/', boot_loader_src])

    except Exception as e:
        print(f"Erreur lors de la configuration du bootloader : {e}")


def nvidia_drivers():
    try:
        bootloaders()
        mkinitcpio()
        hook()

        subprocess.run(['yay', '-S', '--needed', '--noconfirm', 'nvidia-dkms', 'nvidia-utils', 'lib32-nvidia-utils',
                        'nvidia-settings', 'vulkan-icd-loader', 'lib32-vulkan-icd-loader', 'cuda'],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    except Exception as e:
        print(f"Erreur lors de l'installation des pilotes NVIDIA : {e}")
