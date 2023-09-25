#!/usr/bin/env bash

sudo -i

function main() {
    echo "fastestmirror=true" >> /etc/dnf/dnf.conf
    echo "max_parallel_downloads=10" >> /etc/dnf/dnf.conf

    dnf clean all
    dnf upgrade -y

    fwupdmgr refresh
    fwupdmgr get-updates && fwupdmgr update

    dnf install -y --nogpgcheck https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm
    dnf install -y rpmfusion-free-appstream-data rpmfusion-nonfree-appstream-data 
    dnf install -y rpmfusion-free-release-tainted rpmfusion-nonfree-release-tainted

    dnf install -y gstreamer1-plugins-{base,good,bad-free,good-extras,bad-free-extras,ugly-free} gstreamer1-libav
    dnf install -y gstreamer1-plugins-{bad-freeworld,ugly}
    dnf install -y libdvdcss

    dnf -y swap mesa-va-drivers mesa-va-drivers-freeworld
    dnf -y swap mesa-vdpau-drivers mesa-vdpau-drivers-freeworld

    dnf insall steam lutris wine
}

main
