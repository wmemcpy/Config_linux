import subprocess
import os

def config_pacman():
    uncomment: list[str] = ["#VerbosePkgLists", "#ParallelDownloads", "#Color"]
    pacman_src: str = "/etc/pacman.conf"

    with open(pacman_src, "r") as infile, open(pacman_src + ".tmp", "w") as outfile:
        for line in infile:
            if any(line.startswith(s) for s in uncomment):
                outfile.write(line[1:])
            else:
                outfile.write(line)

    os.rename(pacman_src + ".tmp", pacman_src)


def install_kernel_headers():
    try:
        kernels = [f for f in os.listdir('/boot') if f.startswith('vmlinuz')]
        for kernel in kernels:
            kernel_name = kernel.replace('vmlinuz-', '')
            subprocess.run(['sudo', 'pacman', '-S', '--needed', '--noconfirm', f"{kernel_name}-headers"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception as e:
        print(f"Erreur : {e}")


def install_server_sound():
    remove_packages = [
        "pulseaudio",
        "jack2",
        "pipewire-media-session",
        "pulseaudio-bluetooth",
        "pulseaudio-alsa"
    ]
    install_packages = [
        "pipewire",
        "lib32-pipewire",
        "pipewire-pulse",
        "pipewire-alsa",
        "pipewire-jack",
        "wireplumber"
    ]

    for package in remove_packages:
        subprocess.run(['sudo', 'pacman', '-Rdd', '--noconfirm', package], stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL)

    install_command = ['sudo', 'pacman', '-S', '--needed', '--noconfirm'] + install_packages
    subprocess.run(install_command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def install_firewall():
    subprocess.run(['yay', '-S', '--needed', '--noconfirm', 'ufw'], stdout=subprocess.DEVNULL,
                   stderr=subprocess.DEVNULL)

    service_status_result = subprocess.run(['sudo', 'systemctl', 'is-active', 'ufw.service'], stdout=subprocess.PIPE,
                                           text=True)
    if service_status_result.stdout.strip() != 'active':
        subprocess.run(['sudo', 'systemctl', 'enable', '--now', 'ufw.service'], stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL)
