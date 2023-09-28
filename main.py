#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import urwid
import os

os.system("sudo -v")

categories: dict = {"Environnement de bureau": ["KDE", "i3", "gnome"],
                    "Carte graphique": ["AMD", "Intel", "Nvidia"],
                    "Imprimantes": ["Imprimantes non HP/EPSON", "HP", "EPSON"],
                    "Customisation": ["fish", "zsh"]}
selected: dict = {category: [False] * len(options) for category, options in categories.items()}
result: dict = {}


def detecter_distribution():
    if os.path.exists('/etc/os-release'):
        with open('/etc/os-release', 'r') as f:
            for line in f.readlines():
                if line.startswith('ID='):
                    distribution = line.split('=')[1].strip().lower()
                    return distribution
    return None


def modifier_categories(distribution, categories):
    if distribution == 'arch' or distribution == 'archlinux':
        categories["Gestionnaire d'AUR"] = ["yay", "paru"]


class CustomCheckBox(urwid.CheckBox):
    def __init__(self, label, category, index):
        super().__init__(label)
        self.category = category
        self.index = index

    def toggle_state(self):
        super().toggle_state()
        selected[self.category][self.index] = not selected[self.category][self.index]


def execute_scripts(button):
    global result
    result = {category: {option: selected[category][i] for i, option in enumerate(options)} for category, options in
              categories.items()}
    clear_and_exit(button)


def clear_and_exit(button):
    # os.system('clear')
    raise urwid.ExitMainLoop()


def create_menu():
    items: list = []
    for category, options in categories.items():
        items.append(urwid.Text(category))
        for i, option in enumerate(options):
            checkbox = CustomCheckBox(option, category, i)
            items.append(checkbox)
    items.append(urwid.Divider())
    items.append(urwid.Button("Installer", on_press=execute_scripts))
    items.append(urwid.Button("Annuler", on_press=clear_and_exit))
    return urwid.ListBox(urwid.SimpleFocusListWalker(items))


if __name__ == '__main__':
    distro: str = detecter_distribution()
    print(f"{distro} détectée.")
    modifier_categories(distro, categories)

    menu = create_menu()
    loop = urwid.MainLoop(menu)
    loop.run()

    print(result)
    log_file.close()
