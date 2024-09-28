from django.urls import path

from . import views  # Importe les vues définies dans le fichier views.py

# Définition des URL pour l'application. 
# Chaque URL est liée à une vue spécifique qui gère la logique pour cette route.

urlpatterns = [
    # URL pour la page de connexion, qui utilise la vue 'login_view'.
    # Accessible via '/login/' et nommée 'login' pour faciliter les redirections dans le code.
    path('login/', views.login_view, name='login'),

    # URL pour la page d'accueil, qui utilise la vue 'home_view'.
    # Accessible via la racine du site ('/'). Cette route est nommée 'home'.
    path("", views.home_view, name="home"),
]
