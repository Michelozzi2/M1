from django import forms  # Importe le module de formulaires de Django

# Définition d'un formulaire de connexion personnalisé.
# Ce formulaire contient deux champs : un pour le nom d'utilisateur et un pour le mot de passe.

class LoginForm(forms.Form):
    # Champ pour le nom d'utilisateur avec une longueur maximale de 100 caractères.
    username = forms.CharField(label="Nom d'utilisateur", max_length=100)

    # Champ pour le mot de passe. Le widget 'PasswordInput' masque le texte entré.
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
