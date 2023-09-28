from subprocess import CalledProcessError
from src.run_command import run_command

def install_lst(chemin_fichier: str, gestionnaire_paquets: str):
    try:
        with open(chemin_fichier, 'r') as fichier:
            for ligne in fichier:
                paquet = ligne.strip()

                if not paquet:
                    continue

                print(f"Installation du paquet : {paquet}")
                if gestionnaire_paquets == "flatpak":
                    run_command(f"{gestionnaire_paquets} install -y {paquet}")
                else:
                    run_command(f"{gestionnaire_paquets} -S --needed --noconfirm {paquet}")

    except FileNotFoundError:
        print(f"Erreur: Le fichier {chemin_fichier} n'existe pas.")
    except PermissionError:
        print(f"Erreur: Vous n'avez pas la permission de lire le fichier {chemin_fichier}.")
    except CalledProcessError as e:
        print(f"Erreur lors de l'installation du paquet {paquet}: {e}")
