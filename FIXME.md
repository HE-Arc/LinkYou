# Le fix me

## Installation

- pas de procédure d'installation (vaguement de configuration dans le wiki)
- version de django obsolète (CVE) -

## Python

- urls.py dit ceci `(?P<pk>\w+)` et le code fait `int(pk)`
- mettre plus d'urls dans le fichier principal
- le `$` dans les urls est important!
- SELECT N+1
- on ne fait pas de `render` en POST, mais uniquement redirect.
- déclencher les requêtes SQL depuis les templates implique des doublons!
- modèle BlackList non utilisé. (YAGNI)
- ça manque de `get_user_model()`
- modèle Profile non utilisé, Et un UserProfileView inutile. (YAGNI)
- j'aurais séparé le profil de la gestion des collections, liens dans une autre application django.

## UX

- quel est cet effet bizarre sur le bouton "discover collections"
- Linkyou et Home remplissent le même rôle, mais Linkyou contient '#'
- Linkyou, linkyou ou LinkYou ?
- si on saisit un lien sans titre, il n'est pas ajouté
- lorsqu'on édite un lien, on perd le contexte de la collection en cours.
- vous auriez pu faire plus simple et plus efficace en mettant les tags sur le lien
- on recherche pas tags mais les tags n'apparaissent pas dans les résultats
- on n'a pas accès à l'édition d'une collection depuis la collection elle-même, dommage.
- update et delete qui sont si proche est si similaire l'un de l'autre /!\
- delete propose de confirmer mais pas d'annuler ;-)
- pas de navigation par tags, ils font jolis.
- C'est des fois pk-slug, et d'autres slug-pk !? Manque de cohérence dans les urls.
- les favicons sont téléchargés en HTTP!
