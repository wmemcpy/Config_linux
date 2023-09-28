from src.run_command import run_command

def install_intel(aur: str, log: bool=False, log_file: str=None):
    run_command(f"{aur} -S --needed --noconfirm mesa lib32-mesa vulkan-radeon lib32-vulkan-radeon vulkan-icd-loader lib32-vulkan-icd-loader", log, log_file)
