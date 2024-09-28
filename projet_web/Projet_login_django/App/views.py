from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

# Vue pour la page de connexion
def login_view(request):
    # Vérifie si la méthode de la requête est POST (soumission du formulaire)
    if request.method == 'POST':
        # Récupère le nom d'utilisateur et le mot de passe soumis par le formulaire
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Essaye de récupérer l'utilisateur correspondant au nom d'utilisateur fourni
        try:
            user = User.objects.get(user_login=username)
            
            # Vérifie si le mot de passe est correct
            if user.user_password == password:
                # Si correct, stocke l'ID utilisateur et le login dans la session
                request.session['user_id'] = user.user_id
                request.session['user_login'] = user.user_login
                # Redirige vers la page d'accueil
                return redirect('home')
            else:
                # Si le mot de passe est incorrect, affiche un message d'erreur
                messages.error(request, 'Mot de passe incorrect')
        except User.DoesNotExist:
            # Si l'utilisateur n'existe pas, affiche un message d'erreur
            messages.error(request, 'Utilisateur non trouvé')

    # Si la méthode est GET ou en cas d'erreur, affiche la page de connexion
    return render(request, 'pages/login.html')


# Vue pour la page d'accueil (après connexion)
def home_view(request):
    # Récupère le login de l'utilisateur à partir de la session
    user_login = request.session.get('user_login')

    # Si l'utilisateur est connecté, affiche la page d'accueil avec son login
    if user_login:
        return render(request, 'pages/home.html', {'user_login': user_login})
    else:
        # Si l'utilisateur n'est pas connecté, redirige vers la page de connexion
        return redirect('login')
