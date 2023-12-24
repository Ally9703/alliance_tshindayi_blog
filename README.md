# BLOG ALLIANCE TSHINDAYI

Bienvenue dans la documentation de [Alliance TSHINDAYI Blog] !

## Description

Bienvenue dans le blog [Alliance Tshindayi Blog] ! Notre plateforme offre une expérience de blogging simple et élégante, vous permettant de partager vos idées et vos passions avec le monde.

## Installation

1. **Clonez le dépôt :**

    ```bash
    git clone https://github.com/Ally9703/blog_django_projet2.git
    ```

2. **Installez les dépendances :**

    ```bash
    cd blog_django_projet2
    pip install -r requirements.txt
    ```

3. **Effectuez les migrations :**

    ```bash
    python manage.py migrate
    ```

4. **Créez un superutilisateur :**

    ```bash
    python manage.py createsuperuser

    ```

    Suivez les instructions pour créer un compte administrateur.

5. **Lancez le serveur de développement :**

    ```bash
    python manage.py runserver
    ```

    Accédez à l'application à l'adresse http://127.0.0.1:8000/ dans votre navigateur.

## Fonctionnalités

- **Ajout d'Article :** Permet aux utilisateurs de créer et de publier de nouveaux articles.
- **Modification d'Article :** Autorise la mise à jour du contenu des articles existants.
- **Suppression d'Article :** Offre la possibilité de supprimer des articles.
- **Commentaires :** Les utilisateurs peuvent laisser des commentaires sur les articles.

## Utilisation

1. **Accès à l'interface d'administration :**

    - Visitez http://127.0.0.1:8000/admin/
    - Connectez-vous en utilisant le compte superutilisateur créé précédemment.

2. **Gestion des Articles :**

    - Pour ajouter un nouvel article, utilisez l'option "Ajouter" dans la section "Articles".
    - Pour modifier ou supprimer un article existant, utilisez les options correspondantes dans la section "Articles".

3. **Consultation du Blog :**

    - Accédez à l'URL principale http://127.0.0.1:8000/ pour parcourir les articles du blog.
    - Laissez des commentaires sur les articles qui vous intéressent.

## Contribution

Si vous souhaitez contribuer à [Alliance Tshindayi Blog], veuillez consulter le fichier CONTRIBUTING.md pour obtenir des informations détaillées sur la manière de contribuer au projet.

## Licence

Ce projet est sous licence [Type de Licence]. Consultez le fichier LICENSE.md pour plus d'informations.
