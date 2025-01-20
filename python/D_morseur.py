import networkx as nx
import matplotlib.pyplot as plt


class Noeud:
    """Classe représentant un nœud dans un arbre binaire."""

    def __init__(self, valeur, gauche=None, droit=None):
        """Constructeur de la classe Noeud.

        Initialise un nœud avec une valeur et deux enfants optionnels.

        :param valeur: Valeur du nœud
        :param gauche: Enfant gauche du nœud
        :param droit: Enfant droit du nœud
        """
        self.valeur = valeur
        self.gauche = gauche
        self.droit = droit

    def __str__(self):
        """Overwrite le str pour retourner la valeur du noeud."""
        return str(self.valeur)


def hauteur(arbre):
    """Calcule et renvoit la hauteur d'un arbre binaire.

    :param arbre: Racine de l'arbre
    :return: Hauteur de l'arbre
    """
    if arbre is None:
        return 0
    else:
        return 1 + max(hauteur(arbre.gauche), hauteur(arbre.droit))


def repr_graph(arbre, size=(8, 8), null_node=False):
    """Visualise la structure d'un arbre binaire via NetworkX et Matplotlib.

    :param arbre: Racine de l'arbre
    :param size: Taille de la figure (largeur, hauteur)
    :param null_node: Si True, trace les liaisons vers les sous-arbres vides
    """
    def parkour(arbre, noeuds, branches, labels, positions, profondeur,
                pos_courante, pos_parent, null_node):
        if arbre is not None:
            noeuds[0].append(pos_courante)
            positions[pos_courante] = (pos_courante, profondeur)
            profondeur -= 1
            labels[pos_courante] = str(arbre.valeur)
            branches[0].append((pos_courante, pos_parent))
            pos_gauche = pos_courante - 2 ** profondeur
            # Appel récursif pour parcourir le sous-arbre gauche
            parkour(arbre.gauche, noeuds, branches, labels, positions,
                    profondeur, pos_gauche, pos_courante, null_node)
            pos_droit = pos_courante + 2 ** profondeur
            # Appel récursif pour parcourir le sous-arbre droit
            parkour(arbre.droit, noeuds, branches, labels, positions,
                    profondeur, pos_droit, pos_courante, null_node)
        elif null_node:
            noeuds[1].append(pos_courante)
            positions[pos_courante] = (pos_courante, profondeur)
            branches[1].append((pos_courante, pos_parent))

    if arbre is None:
        return

    branches = [[]]
    profondeur = hauteur(arbre)
    pos_courante = 2 ** profondeur
    noeuds = [[pos_courante]]
    positions = {pos_courante: (pos_courante, profondeur)}
    labels = {pos_courante: str(arbre.valeur)}

    if null_node:
        branches.append([])
        noeuds.append([])

    profondeur -= 1
    parkour(arbre.gauche, noeuds, branches, labels, positions, profondeur,
            pos_courante - 2 ** profondeur, pos_courante, null_node)
    parkour(arbre.droit, noeuds, branches, labels, positions, profondeur,
            pos_courante + 2 ** profondeur, pos_courante, null_node)

    mon_arbre = nx.Graph()

    if isinstance(size, int):
        size = (size, size)
    plt.figure(figsize=size)

    nx.draw_networkx_nodes(mon_arbre, positions, nodelist=noeuds[0],
                           node_color="white", node_size=550,
                           edgecolors="blue")
    nx.draw_networkx_edges(mon_arbre, positions, edgelist=branches[0],
                           edge_color="black", width=2)
    nx.draw_networkx_labels(mon_arbre, positions, labels)

    if null_node:
        nx.draw_networkx_nodes(mon_arbre, positions, nodelist=noeuds[1],
                               node_color="white", node_size=50,
                               edgecolors="grey")
        nx.draw_networkx_edges(mon_arbre, positions, edgelist=branches[1],
                               edge_color="grey", width=1)

    ax = plt.gca()
    ax.margins(0.1)
    plt.axis("off")
    plt.show()
    plt.close()


def decode_lettre(arbre, code):
    """Décode une lettre à l'aide d'un code binaire.

    :param arbre: Racine de l'arbre
    :param code: Code binaire pour la lettre
    :return: Lettre décodée
    """
    for i in code:
        if i == "-":
            arbre = arbre.droit
        elif i == "°":
            arbre = arbre.gauche
        else:
            return False
    return arbre.valeur


def encode_lettre(lettre, chemin, arbre):
    """Encode une lettre en code binaire.

    :param lettre: Lettre à encoder
    :param chemin: Chemin binaire actuel
    :param arbre: Racine de l'arbre
    :return: Code binaire pour la lettre
    """
    if arbre is None:
        return ""
    elif arbre.valeur == lettre:
        return chemin
    else:
        # Appel récursif pour parcourir le sous-arbre gauche
        chg = encode_lettre(lettre, chemin + "°", arbre.gauche)
        # Appel récursif pour parcourir le sous-arbre droit
        chd = encode_lettre(lettre, chemin + "-", arbre.droit)
    return chg + chd


def encode_message(message, arbre):
    """Encode un message entier en code binaire en utilisant l'arbre.

    :param message: Message à encoder
    :param arbre: Racine de l'arbre
    :return: Message encodé en code binaire
    """
    encrypted = ""
    for i in message:
        i = i.upper()
        if len(encrypted) > 0:
            encrypted += "*"
        encrypted += encode_lettre(i, "", arbre)
    return encrypted + "*"


def decode_message(message_code, arbre):
    """Décode un message codé en binaire en utilisant l'arbre.

    :param message_code: Message encodé en code binaire
    :param arbre: Racine de l'arbre
    :return: Message décodé
    """

    message = ""
    wordlist_tmp = list(message_code.split("/"))
    wordlist = []
    for i in wordlist_tmp:
        wordlist.append(list(i.split("*")))
    for i in wordlist:
        word = ""
        for j in i:
            if j != '':
                word += decode_lettre(arbre, j)
        message += word + " "
    return message


def dictionnaire(arbre, chemin, dico):
    """Génère un dictionnaire des codes binaires pour chaque lettre dans l'arbre.

    :param arbre: Racine de l'arbre
    :param chemin: Chemin binaire actuel
    :param dico: Dictionnaire des codes binaires
    :return: Dictionnaire des codes binaires
    """
    if arbre is not None:
        if arbre.valeur != "":
            dico[arbre.valeur] = chemin
        # Appel récursif pour parcourir le sous-arbre gauche
        dictionnaire(arbre.gauche, chemin + "°", dico)
        # Appel récursif pour parcourir le sous-arbre droit
        dictionnaire(arbre.droit, chemin + "-", dico)
    return dico
    
