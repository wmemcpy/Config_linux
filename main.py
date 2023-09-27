import urwid
import glob
import subprocess
import os

categories = {
    "Environnement de bureau": ["KDE", "i3", "gnome"],
    "Carte graphique": ["AMD", "Intel", "Nvidia"],
    "Imprimantes": ["Imprimantes non HP/EPSON", "HP", "EPSON"],
    "Customisation": ["Fish"]
}

selected = {category: [False] * len(options) for category, options in categories.items()}

class CustomCheckBox(urwid.CheckBox):
    def __init__(self, label, category, index):
        super().__init__(label)
        self.category = category
        self.index = index

    def toggle_state(self):
        super().toggle_state()
        selected[self.category][self.index] = not selected[self.category][self.index]

def find_script_file(option):
    option_lower = option.lower()
    for script_file in glob.glob("./src/arch/*.py"):
        script_name = os.path.basename(script_file)[:-3]
        if script_name.lower() == option_lower:
            return script_name + '.py'
    return None
def execute_scripts(button):
    for category, options in categories.items():
        for i, option in enumerate(options):
            if selected[category][i]:
                script_name = find_script_file(option)
                if script_name:
                    script_path = f"./src/arch/{script_name}"
                    subprocess.run(["python", script_path])
                else:
                    print(f"No script found for {option}")
    clear_and_exit()

def clear_and_exit(button=None):
    os.system('clear')
    raise urwid.ExitMainLoop()

def create_menu():
    items = []
    for category, options in categories.items():
        items.append(urwid.Text(category))
        for i, option in enumerate(options):
            checkbox = CustomCheckBox(option, category, i)
            items.append(checkbox)
    items.append(urwid.Divider())
    items.append(urwid.Button("Installer", on_press=execute_scripts))
    items.append(urwid.Button("Annuler", on_press=clear_and_exit))
    return urwid.ListBox(urwid.SimpleFocusListWalker(items))

menu = create_menu()
loop = urwid.MainLoop(menu)
loop.run()

print(selected)
