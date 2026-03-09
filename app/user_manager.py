class UserManager:
    def __init__(self):  # Correction ici : self au lieu de selfself
        self.users = []

    def add_user(self, username):
        if not username:
            raise ValueError("Le nom d'utilisateur est obligatoire")
        if username in self.users:
            raise ValueError("Utilisateur déjà existant")
        self.users.append(username)

    def remove_user(self, username):
        if username not in self.users:
            raise ValueError("Utilisateur introuvable")
        self.users.remove(username)

    def count_users(self):
        return len(self.users)

def count_total_users(users):
    # Suppression de la variable 'temp' qui ne servait à rien
    return len(users)