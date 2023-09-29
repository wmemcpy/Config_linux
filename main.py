#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from src.archlinux.arch import main as arch_main
from urwid import CheckBox, ExitMainLoop, Divider, Button, ListBox, SimpleFocusListWalker, MainLoop, Text
from os.path import exists
from os import system

categories: dict = {"Environnement de bureau": ["KDE", "i3", "gnome"],
                    "Carte graphique": ["AMD", "Intel", "Nvidia"],
                    "Imprimantes": ["Imprimantes non HP/EPSON", "HP", "EPSON"],
                    "Customisation": ["fish", "zsh"]}
selected: dict = {category: [False] * len(options) for category, options in categories.items()}

result = {}

def detecter_distribution():
    if exists('/etc/os-release'):
        with open('/etc/os-release', 'r') as f:
            for line in f.readlines():
                if line.startswith('ID='):
                    distribution = line.split('=')[1].strip().lower()
                    return distribution
    return None


def modifier_categories(distribution, category):
    if distribution == 'arch' or distribution == 'archlinux':
        category["Gestionnaire d'AUR"] = ["yay", "paru"]


class CustomCheckBox(CheckBox):
    def __init__(self, label, category, index):
        super().__init__(label)
        self.category = category
        self.index = index

    def change_state(self):
        super().toggle_state()
        selected[self.category][self.index] = not selected[self.category][self.index]


def execute_scripts(button):
    global result
    result = {category: {option: selected[category][i] for i, option in enumerate(options)} for category, options in
              categories.items()}

    system('clear')
    print(f"Résultat:\n{result}")
    arch_main()
    clear_and_exit(button)


def clear_and_exit(button):
    raise ExitMainLoop()


def create_menu():
    items: list = []
    for category, options in categories.items():
        items.append(Text(category))
        for i, option in enumerate(options):
            checkbox = CustomCheckBox(option, category, i)
            items.append(checkbox)
    items.append(Divider())
    items.append(Button("Installer", on_press=execute_scripts))
    items.append(Button("Annuler", on_press=clear_and_exit))
    return ListBox(SimpleFocusListWalker(items))


if __name__ == '__main__':
    distro: str = detecter_distribution()
    print(f"{distro} détectée.")
    modifier_categories(distro, categories)

    menu = create_menu()
    loop = MainLoop(menu)
    loop.run()
