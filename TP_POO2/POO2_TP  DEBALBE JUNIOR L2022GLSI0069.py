# Classe représentant une tâche
class Tache:
    def __init__(self, description):
        self.description = description  # La description de la tâche
        self.statut = "à faire"         # Le statut initial de la tâche

    # Méthode pour marquer la tâche comme terminée
    def marquer_terminee(self):
        self.statut = "terminée"

    # Méthode d'affichage de l'objet Tache
    def __str__(self):
        return f"{self.description} [{self.statut}]"


# Classe pour gérer une liste de tâches
class GestionnaireTaches:
    def __init__(self):
        self.liste_taches = []  # Liste des objets Tache

    # Ajouter une nouvelle tâche à la liste
    def ajouter_tache(self, description):
        tache = Tache(description)
        self.liste_taches.append(tache)
        print("✅ Tâche ajoutée avec succès.")

    # Marquer une tâche comme terminée à partir de son index
    def marquer_terminee(self, index):
        if 0 <= index < len(self.liste_taches):
            self.liste_taches[index].marquer_terminee()
            print("✅ Tâche marquée comme terminée.")
        else:
            print("❌ Index invalide.")

    # Afficher uniquement les tâches non terminées
    def afficher_taches_en_cours(self):
        print("\n📋 Tâches en cours :")
        en_cours = [t for t in self.liste_taches if t.statut != "terminée"]
        if not en_cours:
            print("Aucune tâche en cours.")
        else:
            for i, tache in enumerate(en_cours):
                print(f"{i + 1}. {tache}")

    # Supprimer une tâche à partir de son index
    def supprimer_tache(self, index):
        if 0 <= index < len(self.liste_taches):
            tache = self.liste_taches.pop(index)
            print(f"🗑️ Tâche supprimée : {tache.description}")
        else:
            print("❌ Index invalide.")

    # Afficher toutes les tâches (terminées ou non)
    def afficher_toutes_les_taches(self):
        print("\n📋 Toutes les tâches :")
        if not self.liste_taches:
            print("Aucune tâche enregistrée.")
        else:
            for i, tache in enumerate(self.liste_taches):
                print(f"{i}. {tache}")


# Fonction principale du programme avec menu interactif
def menu():
    gestionnaire = GestionnaireTaches()  # Création d'un gestionnaire de tâches

    while True:
        # Affichage du menu principal
        print("\n=== MENU ===")
        print("1. Ajouter une tâche")
        print("2. Marquer une tâche comme terminée")
        print("3. Afficher les tâches en cours")
        print("4. Supprimer une tâche")
        print("5. Afficher toutes les tâches")
        print("0. Quitter")

        # Saisie du choix de l'utilisateur
        choix = input("Entrez votre choix : ")

        # Exécution selon le choix de l'utilisateur
        if choix == "1":
            desc = input("Description de la tâche : ")
            gestionnaire.ajouter_tache(desc)

        elif choix == "2":
            gestionnaire.afficher_toutes_les_taches()
            idx = int(input("Indice de la tâche à marquer comme terminée : "))
            gestionnaire.marquer_terminee(idx)

        elif choix == "3":
            gestionnaire.afficher_taches_en_cours()

        elif choix == "4":
            gestionnaire.afficher_toutes_les_taches()
            idx = int(input("Indice de la tâche à supprimer : "))
            gestionnaire.supprimer_tache(idx)

        elif choix == "5":
            gestionnaire.afficher_toutes_les_taches()

        elif choix == "0":
            print("👋 Au revoir !")
            break

        else:
            print("❌ Choix invalide. Essayez encore.")


# Point d'entrée du programme
if __name__ == "__main__":
    menu()
