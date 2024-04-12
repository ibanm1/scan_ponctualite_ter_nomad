# scan_ponctualite_ter_nomad
Python de scan des fiches de ponctualité des lignes normandes au départ/arrivée de PSL et PMP

Utilise les libraires et modules suivants : 

* Requests: Cette bibliothèque est utilisée pour envoyer des requêtes HTTP/1.1 avec des paramètres simples à l'aide d'arguments de mots-clés. Elle facilite l'interaction avec les API Web et les pages Web.!
* BeautifulSoup : Cette bibliothèque est utilisée pour extraire des données à partir de fichiers HTML et XML. Elle fournit des moyens simples pour naviguer, rechercher et modifier la structure du document.
* urllib.request : Ce module est utilisé pour ouvrir des URL. Il fournit une interface semblable à une fonction pour ouvrir des pages Web. Il est souvent utilisé en conjonction avec urllib.parse pour manipuler les URL.
* ssl : Ce module fournit des classes et des fonctions permettant de négocier des connexions SSL (Secure Sockets Layer) et TLS (Transport Layer Security).
* os.path : Ce module fournit des fonctions pour manipuler les chemins de fichiers et de répertoires. Il permet de travailler avec les chemins de manière indépendante du système d'exploitation.
* datetime : Ce module fournit des classes pour manipuler les dates et les heures. Il est utilisé ici pour travailler avec des objets de date et d'heure.

Fonctionnement :
* Envoie une requête URL vers la page https://www.ter.sncf.com/normandie/se-deplacer/info-trafic/ponctualite
* Crée un dossier EXTRACTION SNCF si besoin est
* Liste les URL des fichiers pour les stocker dans un .txt
* Sors tous les URL en balise <a> sur l'URL "ter.sncf.com"
* Vérifie si l'URL a déja été téléchargée
* * Si oui : ne charge pas le PDF
* * Si non : charge le PDF
* Mets à jour la liste (.txt) des fichiers chargés
