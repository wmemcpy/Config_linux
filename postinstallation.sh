#!/usr/bin/env bash

sudo -i

function main() {
    echo "fastestmirror=true" >> /etc/dnf/dnf.conf
    echo "max_parallel_downloads=5" >> /etc/dnf/dnf.conf

    dnf clean all
    dnf upgrade -y

    fwupdmgr refresh
    fwupdmgr get-updates && fwupdmgr update

    dnf install -y --nogpgcheck https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm
    dnf install -y rpmfusion-free-appstream-data rpmfusion-nonfree-appstream-data 
    dnf install -y rpmfusion-free-release-tainted rpmfusion-nonfree-release-tainted

    read -r "Quel carte graphique avez-vous ? (intel, nvidia, amd) : " gpu
    if [[ "${gpu}" == "intel" ]]; then
        sudo dnf install intel-media-driver
    elif [[ "${gpu}" == "nvidia" ]]; then
        sudo touch /etc/dracut.conf.d/nvidia.conf
        sudo echo "force_drivers+=" nvidia nvidia_modeset nvidia_uvm nvidia_drm "" >> /etc/dracut.conf.d/nvidia.conf
        sudo dracut --force
        sudo dnf install akmod-nvidia libva-vdpau-driver libva-utils xorg-x11-drv-nvidia-libs xorg-x11-drv-nvidia-cuda vulkan
    elif [[ "${gpu}" == "amd" ]]; then
        sudo dnf install mesa-libOpenCL mesa-libd3d mesa-va-drivers mesa-vdpau-drivers hip hip-devel hsakmt rocm-clinfo rocm-cmake rocm-comgr rocm-device-libs rocm-hip rocm-hip-devel rocm-opencl rocm-opencl-devel rocm-runtime rocm-smi rocminfo
        
    fi

    dnf install -y gstreamer1-plugins-{base,good,bad-free,good-extras,bad-free-extras,ugly-free} gstreamer1-libav
    dnf install -y gstreamer1-plugins-{bad-freeworld,ugly}
    dnf install -y libdvdcss

    dnf -y swap mesa-va-drivers mesa-va-drivers-freeworld
    dnf -y swap mesa-vdpau-drivers mesa-vdpau-drivers-freeworld

    dnf insall steam lutris wine
    dnf swap mesa-va-drivers.i686 mesa-va-drivers-freeworld.i686
    dnf swap mesa-vdpau-drivers.i686 mesa-vdpau-drivers-freeworld.i686
    dnf swap ffmpeg-free ffmpeg --allowerasing
    flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
}

main
