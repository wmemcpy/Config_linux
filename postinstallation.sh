#!/usr/bin/env bash

RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m'

set -x

sudo -i

function main() {
    echo "fastestmirror=true" >> /etc/dnf/dnf.conf
    echo "max_parallel_downloads=5" >> /etc/dnf/dnf.conf

    dnf clean all >> /dev/null 2>&1
    dnf upgrade -y >> /dev/null 2>&1

    fwupdmgr refresh >> /dev/null 2>&1
    fwupdmgr get-updates && fwupdmgr update >> /dev/null 2>&1

    dnf install -y --nogpgcheck https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm >> /dev/null 2>&1
    dnf install -y rpmfusion-free-appstream-data rpmfusion-nonfree-appstream-data >> /dev/null 2>&1
    dnf install -y rpmfusion-free-release-tainted rpmfusion-nonfree-release-tainted >> /dev/null 2>&1

    read -r "Quel carte graphique avez-vous ? (intel, nvidia, amd) : " gpu
    if [[ "${gpu}" == "intel" ]]; then
        sudo dnf install intel-media-driver
    elif [[ "${gpu}" == "nvidia" ]]; then
        sudo touch /etc/dracut.conf.d/nvidia.conf
        sudo echo "force_drivers+=" nvidia nvidia_modeset nvidia_uvm nvidia_drm "" >> /etc/dracut.conf.d/nvidia.conf
        sudo dracut --force
        sudo dnf install -y akmod-nvidia libva-vdpau-driver libva-utils xorg-x11-drv-nvidia-libs xorg-x11-drv-nvidia-cuda vulkan
    elif [[ "${gpu}" == "amd" ]]; then
        sudo dnf install -y mesa-libOpenCL mesa-libd3d mesa-va-drivers mesa-vdpau-drivers hip hip-devel hsakmt rocm-clinfo rocm-cmake rocm-comgr rocm-device-libs rocm-hip rocm-hip-devel rocm-opencl rocm-opencl-devel rocm-runtime rocm-smi rocminfo
    fi

    dnf install -y gstreamer1-plugins-{base,good,bad-free,good-extras,bad-free-extras,ugly-free} gstreamer1-libav >> /dev/null 2>&1
    dnf install -y gstreamer1-plugins-{bad-freeworld,ugly} >> /dev/null 2>&1
    dnf install -y libdvdcss >> /dev/null 2>&1

    dnf -y swap mesa-va-drivers mesa-va-drivers-freeworld >> /dev/null 2>&1
    dnf -y swap mesa-vdpau-drivers mesa-vdpau-drivers-freeworld >> /dev/null 2>&1

    dnf install -y steam lutris wine mangohud goverlay

    dnf swap mesa-va-drivers.i686 mesa-va-drivers-freeworld.i686 >> /dev/null 2>&1
    dnf swap mesa-vdpau-drivers.i686 mesa-vdpau-drivers-freeworld.i686 >> /dev/null 2>&1
    dnf swap ffmpeg-free ffmpeg --allowerasing >> /dev/null 2>&1
}

main
