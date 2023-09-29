from src.run_command import run_command

def enable_fastest_mirror():
    try:
        with open('/etc/dnf/dnf.conf', 'a') as dnf_conf:
            dnf_conf.write("fastestmirror=true\n")
            dnf_conf.write("max_parallel_downloads=5\n")
    except Exception as e:
        print(f"Erreur lors de l'écriture dans le fichier /etc/dnf/dnf.conf : {e}")

def update_system():
    run_command(['dnf', 'clean', 'all'])
    run_command(['dnf', 'upgrade', '-y'])
    run_command(['fwupdmgr', 'refresh'])
    run_command(['fwupdmgr', 'get-updates'])
    run_command(['fwupdmgr', 'update'])

def install_rpmfusion_repos():
    fedora_version = subprocess.check_output(["rpm", "-E", "%fedora"]).decode().strip()
    rpmfusion_repos = [
        f'https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-{fedora_version}.noarch.rpm',
        f'https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-{fedora_version}.noarch.rpm'
    ]
    for repo in rpmfusion_repos:
        run_command(['dnf', 'install', '-y', '--nogpgcheck', repo])

def install_graphics_driver():
    try:
        gpu = input("Quelle carte graphique avez-vous ? (intel, nvidia, amd) : ")
        if gpu == "intel":
            run_command(['dnf', 'install', '-y', 'intel-media-driver'])
        elif gpu == "nvidia":
            run_command(['touch', '/etc/dracut.conf.d/nvidia.conf'])
            run_command(['echo', '"force_drivers+=" nvidia nvidia_modeset nvidia_uvm nvidia_drm "', '>>', '/etc/dracut.conf.d/nvidia.conf'])
            run_command(['dracut', '--force'])
            run_command(['dnf', 'install', '-y', 'akmod-nvidia', 'libva-vdpau-driver', 'libva-utils', 'xorg-x11-drv-nvidia-libs', 'xorg-x11-drv-nvidia-cuda', 'vulkan'])
        elif gpu == "amd":
            run_command(['dnf', 'install', '-y', 'mesa-libOpenCL', 'mesa-libd3d', 'mesa-va-drivers', 'mesa-vdpau-drivers', 'hip', 'hip-devel', 'hsakmt', 'rocm-clinfo', 'rocm-cmake', 'rocm-comgr', 'rocm-device-libs', 'rocm-hip', 'rocm-hip-devel', 'rocm-opencl', 'rocm-opencl-devel', 'rocm-runtime', 'rocm-smi', 'rocminfo'])
    except Exception as e:
        print(f"Erreur lors de l'installation du driver graphique : {e}")

def install_multimedia_packages():
    packages = [
        'gstreamer1-plugins-base', 'gstreamer1-plugins-good', 'gstreamer1-plugins-bad-free',
        'gstreamer1-plugins-good-extras', 'gstreamer1-plugins-bad-free-extras', 'gstreamer1-plugins-ugly-free',
        'gstreamer1-libav', 'gstreamer1-plugins-bad-freeworld', 'gstreamer1-plugins-ugly', 'libdvdcss'
    ]
    run_command(['dnf', 'install', '-y'] + packages)

# Install gaming
def install_gaming_software():
    try:
        with open('../lst/flatpak.lst', 'r') as file:
            content = file.read()
            for flatpak in content.splitlines():
                subprocess.run(['flatpak', 'install', 'flathub', '-y', flatpak], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception as e:
        print(f"Erreur lors de l'installation des logiciels : {e}")

def main():
    enable_fastest_mirror()
    update_system()
    install_rpmfusion_repos()
    install_graphics_driver()
    install_multimedia_packages()
    install_gaming_software()