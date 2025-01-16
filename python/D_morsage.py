# classe Noeud
class Noeud:
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
    
#################### Code pour afficher l'arbre
import networkx as nx
import matplotlib.pyplot as plt

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

###########################################################################################################################################
d = Noeud('d',None,None)
a = Noeud('a',None,None)
c = Noeud('c',None,None)
rg = Noeud('1',a,None)
rd= Noeud('2',c,d)
arbre1 = Noeud('racine',rg,rd)
repr_graph(arbre1,(3,3),True)

###########################################################################################################################################
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
repr_graph(alpharbre,(10,10),True)

###########################################################################################################################################
def decode_lettre(arbre,code):
    for i in code:
        if i == "-":
            arbre = arbre.droit
        elif i == "°":
            arbre = arbre.gauche
        else:
            return False
    return arbre.valeur

print(decode_lettre(alpharbre,'-°-°'))

###########################################################################################################################################
def encode_lettre(lettre,chemin,arbre):
    if arbre is None:
        return ""
    elif arbre.valeur == lettre:
        return chemin
    else:
        chg = encode_lettre(lettre, chemin + "°", arbre.gauche)
        chd = encode_lettre(lettre, chemin + "-", arbre.droit)
    return chg + chd

print(encode_lettre('R',"",alpharbre))

###########################################################################################################################################
def encode_message(message,arbre):
    encrypted=""
    for i in message:
        i=i.upper()
        if len(encrypted)>0:
            encrypted+="*"
        encrypted+=encode_lettre(i, "", alpharbre)
    return encrypted+"*"
print(encode_message('sos', alpharbre))

###########################################################################################################################################
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

###########################################################################################################################################
print("\nA faire 5 donne :", decode_message(
    '-°°°*°-°*°-*°°°-*---*/*°---*°*°°-*-°*°*/*°--°*°-*-°°*°-*°--*°-*-°*/*°-°°*°-*/*-°*°°°*°°*/*°*°°°*-*/*°-*°°°-*°*-°-°*/*-*---*°°*',
    alpharbre))

###########################################################################################################################################
def dictionnaire(arbre,chemin,dico):
    if arbre is not None:
        if arbre.valeur != "":
            dico[arbre.valeur] = chemin
        dictionnaire(arbre.gauche,chemin + "°",dico)
        dictionnaire(arbre.droit,chemin + "-",dico)
    return dico

print(dictionnaire(alpharbre,'',{}))
