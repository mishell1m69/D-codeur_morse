"""Ce fichier correspond à l'intégrité du tp 
fait avant même la distribution du projet."""

# classe Noeud
import networkx as nx
import matplotlib.pyplot as plt

class Noeud:
    '''
    C'est la classe Noeud, indispensable pour créer un arbre.
    Création d'une instance noeud:
    noeud = Noeud(valeur(str), gauche(Noeud), droit(Noeud))
    attributs d'instance : valeur, gauche, droit
    '''
    def __init__(self, valeur, gauche = None, droit = None):
        self.valeur = valeur
        self.gauche = gauche
        self.droit = droit
        
    def __str__(self):
        return str(self.valeur)
    
# fonction hauteur
# la hauteur de la racine est ici de 1
# remplacer 0 par -1 si on souhaite une hauteur de 0 pour la racine
def hauteur(arbre):
    if arbre is None:
        return 0
    else:
        return 1 + max(hauteur(arbre.gauche), hauteur(arbre.droit))


def repr_graph(arbre, size=(8,8), null_node=False):
    """Cette fonction sert à représenter un arbre dans une fenêtre séparée.
    
    :param arbre: L'arbre fourni à représenter (de type Noeud)
    :param size: Le tuple de 2 entiers. Si size est int -> (size, size)
    :param null_node: si True, trace les liaisons vers les sous-arbres vides
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
    # C'est commenté pour pouvoir afficher l'arbre.
    # plt.close()


"""
# Exemple de création d'un arbre :
d = Noeud('d',None,None)
a = Noeud('a',None,None)
c = Noeud('c',None,None)
rg = Noeud('1',a,None)
rd= Noeud('2',c,d)
arbre1 = Noeud('racine',rg,rd)
repr_graph(arbre1,(3,3),True)
"""


# à faire 1
# Créer la représentation de l'abre morse, on se bornera aux lettres de l'alphabet...
print("\nA faire 1 : C\'est fait")
q=Noeud("Q")
z=Noeud("Z")
y=Noeud("Y")
c=Noeud("C")
x=Noeud("X")
b=Noeud("B")
j=Noeud("J")
p=Noeud("P")
l=Noeud("L")
f=Noeud("F")
v=Noeud("V")
h=Noeud("H")
o=Noeud("O")
g=Noeud("G", z, q)
k=Noeud("K", c, y)
d=Noeud("D", b, x)
w=Noeud("W", p, j)
r=Noeud("R", l)
u=Noeud("U", f)
s=Noeud("S", h, v)
a=Noeud("A", r, w)
i=Noeud("I", s, u)
m=Noeud("M", g, o)
n=Noeud("N", d, k)
e=Noeud("E", i, a)
t=Noeud("T", n, m)
alpharbre=Noeud('Start',e,t)
# On l'affiche, pour le coup :
repr_graph(alpharbre,(10,10),True)

print("\nA faire 2 : Le code -°-° correspond à la lettre : ", end="")


def decode_lettre(arbre,code):
    """Cette fonction sert à obtenir la lettre d'un code morse fourni.
    
    :param arbre: L'arbre de l'alphabet de Morse (de type Noeud)
    :param code: Le code morse de la lettre à décoder (de type str)
    :return: Une lettre qui correspond au code morse fourni (de type str)
    """
    # A faire 2
    for i in code:
        if i == "-":
            arbre = arbre.droit
        elif i == "°":
            arbre = arbre.gauche
        else:
            return False
    return arbre.valeur

# Test :
print(decode_lettre(alpharbre,'-°-°'))


def encode_lettre(lettre,chemin,arbre):
    """Cette fonction sert à obtenir le code morse d'une lettre fournie.
    
    :param lettre: La lettre à encoder (de type str)
    :param chemin: La variable permettant de composer un code Morse (de type str)
    :param arbre: L'arbre de l'alphabet morse (de type Noeud)
    :return: Le code morse de la lettre fournie par l'utilisateur (de type str)
    """
    if arbre is None:
        return ""
    elif arbre.valeur == lettre:
        return chemin
    else:
        chg = encode_lettre(lettre, chemin + "°", arbre.gauche)
        chd = encode_lettre(lettre, chemin + "-", arbre.droit)
    return chg + chd


# Test :
print(encode_lettre('R',"",alpharbre))


def encode_message(message,arbre):
    """

    :param message: Une phrase à encoder (de type str)
    :param arbre: L'arbre de l'alphabet de Morse (de type Noeud)
    :return: Le code morse d'une phrase fourni par l'utilisateur (de type str)
    """
    # A faire 3
    encrypted = ""
    for i in message:
        if i != " ":
            i = i.upper()
        else:
            encrypted += "/"
        if len(encrypted)>0:
            encrypted += "*"
        encrypted += encode_lettre(i, "", alpharbre)
    return encrypted + "*"


print("\nA faire 3 : La phrase \'sos\' en code morse est : ", end="")
print(encode_message('sos', arbre_alphabet_morse))


def decode_message(message_code, arbre):
    """Cette fonction sert à obtenir 
    
    :param message_code: Le code morse d'une phrase fourni par l'utilisateur (de tyoe str)
    :param arbre: L'arbre de l'alphabet de Morse (de type Noeud)
    :return: La phrase en français du code morse fourni (de type str)
    """
    # à faire 4
    message = ""
    wordlist_tmp = list(message_code.split("/"))
    wordlist = []
    for i in wordlist_tmp:
        wordlist.append(list(i.split("*")))
    for i in wordlist:
        word = ""
        for j in i:
            if j != '':
                word += decode_lettre(alpharbre, j)
        message += word + " "
    return message


print("\nA faire 5 donne :", decode_message('-°°°*°-°*°-*°°°-*---*/*°---*°*°°-*-°*°*/*°--°*°-*-°°*°-*°--*°-*-°*/*°-°°*°-*/*-°*°°°*°°*/*°*°°°*-*/*°-*°°°-*°*-°-°*/*-*---*°°*', alpharbre))

print("\nA faire 6 :")


def dictionnaire(arbre,chemin,dico):
    if arbre is not None:
        if arbre.valeur != "":
            dico[arbre.valeur] = chemin
        dictionnaire(arbre.gauche,chemin + "°",dico)
        dictionnaire(arbre.droit,chemin + "-",dico)
    return dico


arbre_dict = dictionnaire(arbre_alphabet_morse, '', {})
print(arbre_dict)
print("La fonction est-elle récursive ? si oui, préciser la condition d'arrêt. "
      "Réponse : Elle est récursive car elle fait appel à elle-même. "
      "La condition d\'arrêt est \"if arbre is not None\" ")
print("La fonction parcours l'arbre, de quel parcours s'agit-il ? "
      "Réponse : il s\'agit du parcours préfixe")

print("\nc) codage/decodage par dictionnaire + perf :\n")


def dict_decode_message(arbre, message_code):
    """Cette fonction sert à décoder le message morse (par dictionnaire).

    :param arbre: L'alphabet morse défini par un dictionnaire (de type dict)
    :param message_code: Un code morse fourni à décoder (de type str)
    :return: Renvoie un message décodé sous forme d'une phrase en français.
    """
    decoded_msg = ''
    # On crée un autre dictionaire de l'aphabet morse
    # pour pouvoir décoder le message plus rapidement.
    tmp_dict = dict()
    tmp_message_code = list(message_code.split("/"))
    for cle, valeur in arbre.items():
        # On inverse les cles et les valeurs de l'arbre défini par dict.
        # Pour pouvoir directement et plus facilement retrouver une lettre.
        tmp_dict[valeur] = cle
    for i in tmp_message_code:
        tmp_lettre = ""
        for j in i:
            if j == '*':
                decoded_msg += tmp_dict[tmp_lettre]
                tmp_lettre = ""
            else:
                tmp_lettre += j
        decoded_msg += " "
    return decoded_msg


# Test :
print("On decode le message "
      "-°°°*°-°*°-*°°°-*---*/*°---*°*°°-*-°*°*/*°--°*°-*-°°*°-*°--*°-*-°*/*°-°°*°-*/*-°*°°°*°°*/*°*°°°*-*/*°-*°°°-*°*-°-°*"
      "/*-*---*°°* par dict et on obtient :", dict_decode_message(arbre_dict, '-°°°*°-°*°-*°°°-*---*/*°---*°*°°-*-°*°*/*°--°*°-*-°°*°-*°--*°-*-°*/*°-°°*°-*/*-°*°°°*°°*/*°*°°°*-*/*°-*°°°-*°*-°-°*/*-*---*°°*'))


def dict_encode_message(arbre, message):
    """
    Cette fonction sert à coder un message en code morse (par dictionnaire)

    :param arbre: L'alphabet morse défini par un dictionnaire (de type dict)
    :param message: Un message fourni et à encoder (de type str)
    :return: Renvoie un message sous forme d'un code morse.
    """
    encoded_msg = ''
    message = message.lower()
    for i in message:
        if i == ' ':
            encoded_msg += '/'
        else:
            encoded_msg += arbre[i]
            encoded_msg += '*'
    return encoded_msg


# Test :
print("On encode ensuite la phrase \'sos sos sos sos sos sos sos sos\' par dict et on obtient :", dict_encode_message(arbre_dict, 'sos sos sos SOS sos sos sos SOS'))
