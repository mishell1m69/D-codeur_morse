"""Ce fichier est destiné à l'interface du site Web."""
from time import perf_counter as pf


#  /$$$$$$            /$$                                    
# /$$__  $$          | $$                                    
#| $$  \ $$  /$$$$$$ | $$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$$
#| $$$$$$$$ /$$__  $$| $$__  $$ /$$__  $$ /$$__  $$ /$$_____/
#| $$__  $$| $$  \__/| $$  \ $$| $$  \__/| $$$$$$$$|  $$$$$$ 
#| $$  | $$| $$      | $$  | $$| $$      | $$_____/ \____  $$
#| $$  | $$| $$      | $$$$$$$/| $$      |  $$$$$$$ /$$$$$$$/
#|__/  |__/|__/      |_______/ |__/       \_______/|_______/ 


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


# Création de l'arbre de l'alphabet Morse 
# comprenant les caractères, les chiffres,  
# ainsi que les signes de ponctuation.
parenthese_fermantre = Noeud(')')
parenthese_ouvrante = Noeud('(', None, parenthese_fermantre)
y = Noeud('y', parenthese_ouvrante)
point_virgule = Noeud(';')
none_c_droit = Noeud('', point_virgule)
cedile = Noeud('ç')
c = Noeud('c', cedile, none_c_droit)
k = Noeud('k', c, y)
signe_fraction = Noeud('/')
x = Noeud('x', signe_fraction)
signe_egal = Noeud('=')
signe_moins = Noeud('-')
six = Noeud('6', None, signe_moins)
b = Noeud('b', six, signe_egal)
d = Noeud('d', b, x)
n = Noeud('n', d, k)
g_accent_circonflexe = Noeud('ĝ')
q = Noeud('q', g_accent_circonflexe)
sept = Noeud('7')
virgule = Noeud(',')
none_z_droit = Noeud('', None, virgule)
z = Noeud('z', sept, none_z_droit)
g = Noeud('g', z, q)
neuf = Noeud('9')
zero = Noeud('0')
none_o_droit = Noeud('', neuf, zero)
deux_points = Noeud(':')
huit = Noeud('8', deux_points)
o_trema = Noeud('ö', huit)
o = Noeud('o', o_trema, none_o_droit)
m = Noeud('m', g, o)
t = Noeud('t', n, m)
e_accent_aigu = Noeud('é')
f = Noeud('f', e_accent_aigu)
deux = Noeud('2')
signe_pt_interro = Noeud('?')
tiret_bas = Noeud('_')
eth = Noeud('ð ', signe_pt_interro, tiret_bas)
u_trema = Noeud('ü', eth, deux)
u = Noeud('u', f, u_trema)
trois = Noeud('3')
dollar = Noeud('$')
none_v_gauche_gauche = Noeud('', None, dollar)
none_v_gauche = Noeud('', none_v_gauche_gauche)
v = Noeud('v', none_v_gauche, trois)
quatre = Noeud('4')
cinq = Noeud('5')
h = Noeud('h', cinq, quatre)
s = Noeud('s', h, v)
i = Noeud('i', s, u)
et_commercial = Noeud('&')
guillemet_droit = Noeud('\"')
e_accent_grave = Noeud('è', guillemet_droit)
l = Noeud('l', et_commercial, e_accent_grave)
point = Noeud('.')
signe_plus = Noeud('+', None, point)
a_e_entrelace = Noeud('æ', signe_plus)
r = Noeud('r', l, a_e_entrelace)
signe_apostrophe = Noeud('\'')
un = Noeud("1", signe_apostrophe)
j = Noeud('j', None, un)
arobase = Noeud('@')
a_accent_grave = Noeud('à', arobase)
p = Noeud('p', None, a_accent_grave)
w = Noeud('w', p, j)
a = Noeud('a', r, w)
e = Noeud('e', i, a)
arbre_alphabet_morse = Noeud('start', e, t)


def hauteur(arbre):
    """Calcule et renvoie la hauteur d'un arbre binaire.

    :param arbre: Racine de l'arbre
    :return: Hauteur de l'arbre
    """
    if arbre is None:
        return 0
    else:
        return 1 + max(hauteur(arbre.gauche), hauteur(arbre.droit))


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
    #print(arbre.valeur, arbre.gauche, arbre.droit)
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

    t0 = pf()
    encrypted = ""
    for i in message:
        if i == '\n':
            encrypted += "#*"
        elif i != " ":
            i = i.lower()
            lettre = encode_lettre(i, "", arbre)
            if lettre:
                encrypted += lettre + "*"
            else:
                return "Attention, votre message contient au moins un caractère non encodable : " + i, pf() - t0
        else:
            encrypted += "/"
    return encrypted, pf() - t0


def decode_message(message_code, arbre):
    """Décode un message codé en binaire en utilisant l'arbre.

    :param message_code: Message encodé en code binaire
    :param arbre: Racine de l'arbre
    :return: Message décodé
    """

    t0 = pf()
    message = ""
    wordlist_tmp = list(message_code.split("/"))
    wordlist = []
    for i in wordlist_tmp:
        wordlist.append(list(i.split("*")))
    for words in wordlist:
        word = ""
        for i in words:
            if i != '' and i != "#" and i != '\n':
                lettre = decode_lettre(arbre, i)
                if lettre:
                    word += lettre
                else:
                    return "Attention, votre message contient au moins un caractère non décodable : " + i, pf() - t0
            elif i == "#":
                word += '\n'
        message += word + " "
        """if len(word)>0 and word[-1] == '\n':
            message += word
        else:
            message += word + """
    return message, pf() - t0

# /$$$$$$$  /$$             /$$     /$$                                         /$$                              
#| $$__  $$|__/            | $$    |__/                                        |__/                              
#| $$  \ $$ /$$  /$$$$$$$ /$$$$$$   /$$  /$$$$$$  /$$$$$$$  /$$$$$$$   /$$$$$$  /$$  /$$$$$$   /$$$$$$   /$$$$$$$
#| $$  | $$| $$ /$$_____/|_  $$_/  | $$ /$$__  $$| $$__  $$| $$__  $$ |____  $$| $$ /$$__  $$ /$$__  $$ /$$_____/
#| $$  | $$| $$| $$        | $$    | $$| $$  \ $$| $$  \ $$| $$  \ $$  /$$$$$$$| $$| $$  \__/| $$$$$$$$|  $$$$$$ 
#| $$  | $$| $$| $$        | $$ /$$| $$| $$  | $$| $$  | $$| $$  | $$ /$$__  $$| $$| $$      | $$_____/ \____  $$
#| $$$$$$$/| $$|  $$$$$$$  |  $$$$/| $$|  $$$$$$/| $$  | $$| $$  | $$|  $$$$$$$| $$| $$      |  $$$$$$$ /$$$$$$$/
#|_______/ |__/ \_______/   \___/  |__/ \______/ |__/  |__/|__/  |__/ \_______/|__/|__/       \_______/|_______/ 

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


# Création de l'arbre de l'alphabet Morse 
# avec un dictionnaire (de type dict)
arbre_dict = dictionnaire(arbre_alphabet_morse, '', {})


def dict_encode_message(arbre, message):
    """Cette fonction sert à coder un message en code morse (par dictionnaire).

    :param arbre: L'alphabet morse défini par un dictionnaire (de type dict)
    :param message: Un message fourni et à encoder (de type str)
    :return: Renvoie un message sous forme d'un code morse.
    """

    t0 = pf()
    encoded_msg = ''
    for i in message:
        i = i.lower()
        if i == ' ':
            encoded_msg += '/'
        else:
            if i in arbre.keys():
                encoded_msg += arbre[i] + "*"
            else:
                return "Attention, votre message contient au moins un caractère non encodable : " + i, pf() - t0
    return encoded_msg, pf() - t0


def dict_decode_message(arbre, message_code):
    """Cette fonction sert à décoder le message morse (par dictionnaire).

    :param arbre: L'alphabet morse défini par un dictionnaire (de type dict)
    :param message_code: Un code morse fourni à décoder (de type str)
    :return: Renvoie un message décodé sous forme d'une phrase en français.
    """

    t0 = pf()
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
        print("i", i)
        tmp_lettre = ""
        for j in i:
            print("j",j)
            if j == '*':
                if tmp_lettre != '':
                    print(tmp_lettre)
                    if tmp_lettre in tmp_dict.keys():
                        decoded_msg += tmp_dict[tmp_lettre]
                    else:
                        return "Attention, votre message contient au moins un caractère non décodablee : " + tmp_lettre, pf() - t0
                tmp_lettre = ""
            elif j == "-" or j == "°":
                tmp_lettre += j
            else:
                return "Attention, votre message contient au moins un caractère non décodable : " + j, pf() - t0
        decoded_msg += " "
    return decoded_msg, pf() - t0
