import networkx as nx
import matplotlib.pyplot as plt


class Noeud:
    def __init__(self, valeur, gauche = None, droit = None):
        self.valeur = valeur
        self.gauche = gauche
        self.droit = droit

        
    def __str__(self):
        return str(self.valeur)


def hauteur(arbre):
    if arbre is None:
        return 0
    else:
        return 1 + max(hauteur(arbre.gauche), hauteur(arbre.droit))


def repr_graph(arbre, size=(8,8), null_node=False):
    """
    size : tuple de 2 entiers. Si size est int -> (size, size)
    null_node : si True, trace les liaisons vers les sous-arbres vides
    """
    def parkour(arbre, noeuds, branches, labels, positions, profondeur, pos_courante, pos_parent, null_node):
        if arbre is not None:
            noeuds[0].append(pos_courante)
            positions[pos_courante] = (pos_courante, profondeur)
            profondeur -= 1
            labels[pos_courante] = str(arbre.valeur)
            branches[0].append((pos_courante, pos_parent))
            pos_gauche = pos_courante - 2**profondeur
            parkour(arbre.gauche, noeuds, branches, labels, positions, profondeur, pos_gauche, pos_courante, null_node)
            pos_droit = pos_courante + 2**profondeur
            parkour(arbre.droit, noeuds, branches, labels, positions, profondeur, pos_droit, pos_courante, null_node)
        elif null_node:
            noeuds[1].append(pos_courante)
            positions[pos_courante] = (pos_courante, profondeur)
            branches[1].append((pos_courante, pos_parent))
    
    
    if arbre is None:
        return
    
    branches = [[]]
    profondeur = hauteur(arbre)
    pos_courante = 2**profondeur
    noeuds = [[pos_courante]]
    positions = {pos_courante: (pos_courante, profondeur)} 
    labels = {pos_courante: str(arbre.valeur)}
    
    if null_node:
        branches.append([])
        noeuds.append([])
        
    profondeur -= 1
    parkour(arbre.gauche, noeuds, branches, labels, positions, profondeur, pos_courante - 2**profondeur, pos_courante, null_node)
    parkour(arbre.droit, noeuds, branches, labels, positions, profondeur, pos_courante + 2**profondeur, pos_courante, null_node) 

    mon_arbre = nx.Graph()
    
    if type(size) == int:
        size = (size, size)    
    plt.figure(figsize=size)
    
    nx.draw_networkx_nodes(mon_arbre, positions, nodelist=noeuds[0], node_color="white", node_size=550, edgecolors="blue")
    nx.draw_networkx_edges(mon_arbre, positions, edgelist=branches[0], edge_color="black", width=2)
    nx.draw_networkx_labels(mon_arbre, positions, labels)

    if null_node:
        nx.draw_networkx_nodes(mon_arbre, positions, nodelist=noeuds[1], node_color="white", node_size=50, edgecolors="grey")
        nx.draw_networkx_edges(mon_arbre, positions, edgelist=branches[1], edge_color="grey", width=1)

    ax = plt.gca()
    ax.margins(0.1)
    plt.axis("off")
    plt.show()
    plt.close()


def decode_lettre(arbre,code):
    for i in code:
        if i == "-":
            arbre = arbre.droit
        elif i == "°":
            arbre = arbre.gauche
        else:
            return False
    return arbre.valeur


def encode_lettre(lettre,chemin,arbre):
    if arbre is None:
        return ""
    elif arbre.valeur == lettre:
        return chemin
    else:
        chg = encode_lettre(lettre, chemin + "°", arbre.gauche)
        chd = encode_lettre(lettre, chemin + "-", arbre.droit)
    return chg + chd


def encode_message(message,arbre):
    encrypted=""
    for i in message:
        i=i.upper()
        if len(encrypted)>0:
            encrypted+="*"
        encrypted+=encode_lettre(i, "", alpharbre)
    return encrypted+"*"


def decode_message(message_code, arbre):
    message=""
    wordlist_tmp = list(message_code.split("/"))
    wordlist=[]
    for i in wordlist_tmp:
        wordlist.append(list(i.split("*")))
    for i in wordlist:
        word=""
        for j in i:
            if j != '':
                word+=decode_lettre(alpharbre, j)
        message+=word+" "
    return message


def dictionnaire(arbre,chemin,dico):
    if arbre is not None:
        if arbre.valeur != "":
            dico[arbre.valeur] = chemin
        dictionnaire(arbre.gauche,chemin + "°",dico)
        dictionnaire(arbre.droit,chemin + "-",dico)
    return dico


def dict_encode_message(ab_dict, message):
    """
    Cette fonction sert à coder un message en code morse (par dictionnaire)
    :param ab_dict: L'alphabet morse défini par un dictionnaire (de type dict)
    :param message: Un message fourni et à encoder 
    :return: Renvoie un message sous forme d'un code morse.
    """
    encoded_msg = ''
    for i in message:
        if i == ' ':
            encoded_msg += '/'
        else:
            encoded_msg += ab_dict[i]
            encoded_msg += '*'
    return encoded_msg

