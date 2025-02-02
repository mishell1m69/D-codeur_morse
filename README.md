# Le projet sur le code morse
<i>Par APET Vlad, CHALENDARD Jao et MICHEL Clément</i> - Terminale<br><br>
Ce projet présente un programme (une interface Web, pour être plus précis) permettant à l'utilisateur de décoder un code écrit en morse, <br>d'encoder un texte pour obtenir son code morse,
d'encoder ou décoder un fichier (de format .txt) entier (soit en français, soit en code morse), <br>ainsi que de décoder (idem pour encoder) un fichier ou un message à la fois par arbre et par dictionnaire afin de comparer le temps que nécessitent les deux méthodes (par dictionnaire et par arbre) et en déduire celle qui est la plus efficace.
<br>
<br>
Ce projet a été réalisé en Python (avec les bibliothèques: Flask, Networkx, Matplotlib...) pour la partie algorithmique, et en HTML/CSS/JS pour l'interface web.<br>
<br>
Nous avons réalisé des tests de décodage allant jusqu'a 100,000 caractères, et le site n'a présenté aucun signe de faiblesse, et nous supposons que l'on peut atteindre des niveaux de décodages biens supérieurs.<br>

# Précisions préalables
1) Le fichier D_morsage.py correspond au tp et D_morseur.py est le fichier contenant les fonctions et variables indispensables pour l'interface Web. 
2) Les "#*" correspondent aux sauts de ligne présents dans les fichiers (de format .txt) après encodage, ainsi la mise en page est respectée. (ceci est notre propre fonctionnalité développée)
3) Les lettres sont séparées par des '*'  et les espaces sont représentés par des '/' en morse.
4) Les bibliothèques Networkx et matplotlib sont uniquement utiles pour le Tp initial et non pour le site web.
5) Si vous essayez d'encoder un caractère qui n'existe pas en morse, un message vous préviendra et affichera ce caractère soit sur le site soit dans le fichier encodé.
6) Il est possible de 'bypass' la fonction précédente en commençant le texte à encoder par '&&' afin que les caractères intranscribtiples soit totalement ignorés (fonctionnel sur site et fichiers).

# Répartition des tâches & Lancement
<i>VLAD</i> s'est chargé de :<br>
<ul>
  <li>Réaliser le TP initial concernant le projet (cf. le tp mentionné dans les sources)<br></li>
  <li>Implémenter les différents algorithmes de décodage en Python (par arbre et par dictionnaire de manière itérative)</li>
  <li>Implémenter les différents algorithmes de codage en Python (de la même manière que le décodage)</li>
  <li>Améliorer la documentation (docstrings, commentaires)</li>
  <li>Rédiger le README et documenter le projet (ses fonctions, fichiers, etc...)</li>
  <li>Implémenter l'arbre morse avec plus de 65 différents caractères</li>
  <li>Effectuer des tests</li>
</ul>

<i>JAO</i> s'est chargé de :<br>
<ul>
  <li>Améliorer les algorithmes de décodage en Python (assert, saut de ligne...)</li>
  <li>Améliorer les algorithmes de codage en Python (assert, saut de ligne...)</li>
  <li>Gérer les communications des pages HTML, des fonctions Python et des fichiers (.txt) grâce à Flask</li>
  <li>Améliorer le README</li>
  <li>Améliorer le code HTML pour prendre en charge les fichiers (de format .txt)</li>
  <li>Gérer la structure et l'arborescence de nos travaux</li>
  <li>Effectuer des tests</li>
</ul>

<i>CLÉMENT</i> s'est chargé de:<br>
<ul>
  <li>Construire l'entiereté des pages HTML grâce au framework de W3.CSS</li>
  <li>Mettre en place le design du site internet et de toutes ses pages</li>
  <li>Gérer l'aspect "responsive" du site et sa compatibilité sur plusieurs appareils</li>
  <li>Rédiger le README et la documentation globale du projet</li>
  <li>Effectuer des tests</li>
</ul><br>

# Comment lancer le programme?
<ol>
  <li>Assurez vous d'avoir installé la bibliothèque "Flask". Si vous ne l'avez pas, tapez dans la console : <code>pip install Flask</code></li>
  <li>Pour installer la bibliothèque "matplotlib" (non essentielle pour l'interface Web), tapez dans la console : <code>pip install matplotlib</code></li>
  <li>Pour installer la bibliothèque "networkx"(non essentielle pour l'interface Web), tapez dans la console : <code>pip install networkx</code></li>
  <li>Lancer/Exécuter le fichier main.py<br></li>
  <li>Laissez vous guider par le site</li>
  <li>Remplissez les blocs de texte et soumettez-les</li>
  <li>Décodez et encodez vos messages !</li>
</ol><br>

# Sources 
<dl>
  <dt>ayant aidé à la réalisation du HTML/CSS/JS :</dt>
  <dd>W3 Schools CSS : https://www.w3schools.com/w3css/default.asp</dd>
  <dd>UIverse : https://uiverse.io/themrsami/dull-moose-46 et https://uiverse.io/Juanes200122/yellow-zebra-53</dd>
  <dt>ayant aidé à la découverte du code morse :</dt>
  <dd>Wikipedia : https://fr.wikipedia.org/wiki/Code_Morse_international</dd>
  <dt>ayant fourni le tp en question :</dt>
  <dd>nsi-ljm.fr : https://www.nsi-ljm.fr/basthon-notebook/?from=https://www.nsi-ljm.fr/notebook/morseT.ipynb</dd>
</dl>
<br>
MERCI d'avoir pris le temps de lire jusqu'ici, et bonnes découvertes!
<i>CLÉMENT, VLAD & JAO</i>
