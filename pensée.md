Je veux simplifier MenuDeplacement en le rendant plus lisible.

### Raisonnement

Si je réduis la longueur de certaines instructions tout en conservant la clarté, le code sera plus lisible.

Cette ligne est particulièrement longue "self.monde.obtenir_joueur().obtenir_coordinateur().aller_destination"

Si je transforme cette ligne en "self.fonction_de_deplacement" ou "self.aller_destination", le code est toujours tout aussi clair.

Si je transforme cette ligne en "self.joueur.aller_destination", l'intention du code est d'autant plus clair.

Afin de faire cela, j'ai deux options principales :
    - Passer en tant que paramètres du constructeur MenuDeplacement l'objet "joueur"
    - Obtenir l'objet "joueur" depuis un appel de la méthode "monde"

~~Le principal avantage de la première méthode est qu'elle permet d'accéder à l'objet "joueur" sans dépendre de l'existence d'une méthode de "monde".~~

L'avantage principal de la première option est que je peux supprimer toutes les références à "monde" dans le code de cette classe. Cela rend le code de la classe moins verbeux.

~~Si je ne dépens pas d'une méthode l'objet "monde", l'objet "monde" n'a pas à implémenter une méthode ayant accès à "joueur".~~
Même si la classe "MenuDeplacement" ne dépend pas d'un objet "monde", l'objet "monde" doit implémenter une méthode donnant "joueur" car elle construit cet objet.

### Conclusion

Je conclus que je peux rendre mon code plus lisible en :
- tranformant les sections "self.monde.obtenir_joueur() ..." en "self.joueur"
- en passant en paramètres l'objet "joueur" à la classe "MenuDeplacement"
- en introduisant une méthode "aller_destination" à la classe Joueur

Afin que le code fonctionne, je dois aussi modifier le constructeur de menu afin qu'il passe en paramètres l'objet "joueur".

### Contre-exemples :
- Je ne réduis pas la taille de certaines instructions
- Cette ligne est particulièrement longue "self.monde.obtenir_joueur().obtenir_coordinateur().aller_destination"
- Je ne transforme pas cette ligne en "self.fonction_de_deplacement" ou "self.aller_destination"
- je ne transforme pas cette ligne en "self.joueur.aller_destination"
- Je peux passer en tant que paramètres du constructeur MenuDeplacement l'objet "joueur"
- Je peux obtenir l'objet "joueur" depuis un appel de la méthode "monde"
- L'avantage principal de la première option est que je peux supprimer toutes les références à "monde" dans le code de cette classe.
- Cela rend le code de la classe moins verbeux.
- Même si la classe "MenuDeplacement" ne dépend pas d'un objet "monde", l'objet "monde" doit implémenter une méthode donnant "joueur" car elle construit cet objet.
- Je ne peux pas rendre mon code plus lisible en tranformant les sections "self.monde.obtenir_joueur() ..." en "self.joueur".
- Je ne peux pas rendre mon code plus lisible en passant en paramètres l'objet "joueur" à la classe "MenuDeplacement"
- Je ne peux pas rendre mon code plus lisible en introduisant une méthode "aller_destination" à la classe Joueur


### Raisonnement 2

Supposons que je souhaite remplacer les sections "self.monde.obtenir_joueur() ..." par "self.joueur".
- Si la variable appelé 'joueur' n'est pas initialisé dans le contexte d'exécution d'une instance de la classe MenuDeplacement, alors je ne peux pas appeler les



### Conclusion

Si je souhaite remplacer les sections "self.monde.obtenir_joueur() ..." par "self.joueur" dans les méthodes de la classe MenuDeplacement sans déclarer  je dois placer paramètres l'objet "joueur" au constructeur de la classe "MenuDeplacement" ou je dois obtenir l'objet "joueur" depuis un appel de la méthode "monde".

