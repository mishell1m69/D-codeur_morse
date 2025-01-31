# Le projet sur le code morse
<i>Par APET Vlad, CHALENDARD Jao et MICHEL Clément</i> - Terminale<br><br>
Ce projet présente un programme (une interface Web, pour être plus précis) permettant à l'utilisateur de décoder un code écrit en morse, <br>d'encoder un texte pour obtenir son code morse,
d'encoder ou décoder un fichier (de format .txt) entier (soit en français, soit en code morse), <br>ainsi que de décoder (idem pour encoder) un fichier ou un message à la fois par arbre et par dictionnaire afin de comparer le temps que nécessitent les deux méthodes (par dictionnaire et par arbre) et en déduire celle qui est la plus efficace.
<br>
<br>
Ce projet a été réalisé en Python (aditionellement, les bibliothèques: Flask, Networkx, Matplotlib...) pour la partie algorithmique, et en HTML/CSS/JS pour l'interface web.<br>
<br>
Nous avons réalisé des tests de décodage allant jusqu'a 100,000 caractères, et le site n'a présenté aucun signe de faiblesse, et nous supposons que l'on peut atteindre des niveaux de décodages biens supérieurs.<br>

# Précisions préalables
1) Le fichier D_morsage.py correspond au tp fait avant même la distribution des projets. <br>Quant au fichier D_morseur.py, c'est le fichier contenant l'arbre, le dictionnaire et les fonctions indispensables pour l'interface Web. 
2) Les "#" (caractère inexistant dans le code morse actuel) obtenus après l'encodage des fichiers correspondent aux sauts de ligne présents dans les fichiers (de format .txt) à encoder, ce qui fait que la mise en page est respectée.
3) Les sauts de lignes sont donc bien pris en compte.

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
  <li>Gérer les communication des pages HTML, des fonctions Python et des fichiers (.txt) grâce à Flask</li>
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
  <li>Renvoyer les résultats des requêtes grâce à Python (Flask) sur HTML</li>
  <li>Effectuer des tests</li>
</ul><br>

# Comment lancer le programme?
<ol>
  <li>Assurez vous d'avoir installé la bibliothèqu "Flask". Si vous ne l'avez pas, tapez dans la console : <code>pip install Flask</code></li>
  <li>Assurez-vous d'avoir installé la bibliothèque "pygame". Si vous ne l'avez pas, tapez dans la console : <code>pip install pygame</code></li>
  <li>Assurez-vous d'avoir installé la bibliothèque "networkx". Si vous ne l'avez pas, tapez dans la console : <code>pip install networkx</code></li>
  <li>Vérifier la présence de la bibliothèque "matplotlib" (pour pouvoir tester le fichier du tp)<br>Si jamais vous ne l'avez pas installée, tapez dans la console <code>pip install matplotlib</code> pour ce faire</li>
  <li>Lancer/Exécuter le fichier main.py<br></li>
  <li>Laissez vous guider par le site</li>
  <li>Remplissez les blocs de texte et exécutez-les</li>
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
