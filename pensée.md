## Premier problème

Je souhaite que les instances de classe externes à mon instance de Joueur ne puissent pas accéder aux composants de Joueur.
Je souhaite aussi que la classe Joueur soit lisible.

### Raisonnement

Si j'espace les méthodes de la classe Joueur et que je les arrange par catégorie, la classe Joueur sera plus lisible.

Si je supprime les méthodes de la classe Joueur qui ne sont pas utilisés, je peux rendre la classe plus lisible.

Si je ne stockes pas les instances de Itineraire et Deplaceur dans l'instance de Joueur, la classe Joueur sera plus lisible.

Si je supprimes les méthodes renvoyant un composant de Joueur, les autres objets ne pourrant pas les accéder.

Si je supprimes les méthodes renvoyant un composant de Joueur et que je souhaite éviter des bugs, je dois introduire de nouvelles méthodes à Joueur pour chaque méthode du composant appellée.

Afin d'introduire les nouvelles méthodes à Joueur pour chaque méthode du composant appellée, je dois faire la liste des méthodes des composants de Joueur appelées.

Afin de savoir quelles méthodes de la classe Joueur ne sont pas utilisées, je dois faire la liste des méthodes de Joueur utilisées.

Si je ne stockes pas les instances de Itineraire et Deplaceur dans la classe Joueur, je dois introduire des méthodes à CoordinateurMouvement afin qu'on puisse intéragir avec ces composants.

Si je souhaite introduire des méthodes à CoordinateurMouvement afin qu'on puisse intéragir avec ces composants, je dois faire la liste des méthodes des composants de CoordinateurMouvement appellées.

Il est préférable que je renvoie la liste des bateaux plutôt qu'introduire des méthodes intermédiaires.

### Conclusion

Je dois :
1. ~~Faire la liste des méthodes de Joueur utilisées~~
2. ~~Supprimer les méthodes de Joueur qui ne sont pas utilisées.~~
3. Faire la liste des méthodes des composants de Joueur appellées à l'extérieur de Joueur (Sauf pour bateau)
4. Introduire des nouvelles méthodes à Joueur pour chaque méthode d'un composant appellée à l'extérieur de Joueur (Sauf pour bateau)
5. Substituer les appels de méthode renvoyant un composant de Joueur par une nouvelle méthode. (Sauf pour bateau)
6. Supprimer les méthodes renvoyant un composant de Joueur (Sauf pour bateau)
7. Faire la liste des méthodes des composants de CoordinateurMouvement appellés à l'extérieur de CoordinateurMouvement
8. Introduire des nouvelles méthodes à CoordinateurMouvement pour chaque méthode d'un composant appellée à l'extérieur de CoordinateurMouvement
9. Subtituer les appels de méthode à un composant de CoordinateurMouvement (à l'extérieur de CoordinateurMouvement) par une nouvelle une nouvelle méthode.
10. Ne plus stocker les composants de CoordinateurMouvement dans Joueur
11. Arranger les méthodes de Joueur par catégorie

## Deuxième problème

### Proposition à étudier

Aucun objet externe à Joueur ne doit pouvoir envoyer des messages à un composant de Joueur sans passer par Joueur.

### Raisonnement

Si aucun objet externe à Joueur envoie de messages à un composant de Joueur sans passer par Joueur, chaque accès à une fonctionnalité d'un composant de Joueur devra passer par Joueur.

Si aucun objet externe à Joueur envoie de messages à un composant de Joueur sans passer par Joueur, les objets externes à Joueur ne pourront plus parcourir directement la liste des bateaux du joueur.

Si chaque accès à une fonctionnalité d'un composant de Joueur doit par Joueur, la classe Joueur devra avoir une méthode pour chacune de ces fonctionalités.

Si aucun objet externe à Joueur envoie de messages à un composant de Joueur sans passer par Joueur, je peux changer la structure interne de Joueur sans casser le code autre part.

Si aucun objet externe à Joueur envoie de messages à un composant de Joueur sans passer par Joueur, la modification du c

