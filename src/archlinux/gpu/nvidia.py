from os import listdir, makedirs
from os.path import isdir, join
from shutil import copyfile

from src.install_lst import install_lst
from src.run_command import run_command


def install_nvidia(aur: str):
    install_lst('../lst/nvidia.lst', aur)

    if isdir('/boot/loader/entries/'):
        for entry in listdir('/boot/loader/entries/'):
            if entry.endswith('.conf'):
                path = join('/boot/loader/entries/', entry)
                with open(path, 'r') as file:
                    content = file.readlines()
                for i, line in enumerate(content):
                    if line.startswith('options'):
                        content[i] = line.rstrip() + ' nvidia-drm.modeset=1\n'
                with open(path, 'w') as file:
                    file.writelines(content)
    else:
        with open('/etc/default/grub', 'r') as file:
            content = file.readlines()
        for i, line in enumerate(content):
            if line.startswith('GRUB_CMDLINE_LINUX_DEFAULT='):
                content[i] = line.rstrip('"') + ' nvidia-drm.modeset=1"\n'
        with open('/etc/default/grub', 'w') as file:
            file.writelines(content)
        run_command('sudo grub-mkconfig -o /boot/grub/grub.cfg')

    with open('/etc/mkinitcpio.conf', 'r') as file:
        content = file.readlines()
    for i, line in enumerate(content):
        if line.startswith('MODULES='):
            content[i] = 'MODULES=(nvidia nvidia_modeset nvidia_uvm nvidia_drm)\n'
    with open('/etc/mkinitcpio.conf', 'w') as file:
        file.writelines(content)

    makedirs('/etc/pacman.d/hooks/', exist_ok=True)
    copyfile('../files/nvidia.hook', '/etc/pacman.d/hooks/nvidia.hook')
