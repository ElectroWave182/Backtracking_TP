global liste
liste = []

global somme

def est_solution (quadruplet):

    x0 = quadruplet[0]
    x1 = quadruplet[1]
    x2 = quadruplet[2]
    x3 = quadruplet[3]

    return x0 != x1 and x2 != x3 and x0 + x2 < x1 and not (quadruplet in liste)


def element_valide (quadruplet, cpt):

    drapeau = True
    x0 = quadruplet[0]
    x1 = quadruplet[1]
    x2 = quadruplet[2]
    x3 = quadruplet[3]

    if cpt == 1:
        drapeau = drapeau and x0 != x1

    if cpt == 2:
        drapeau = drapeau and x0 + x2 < x1

    if cpt == 3:
        drapeau = drapeau and x2 != x3

    return drapeau


def ajout_possible (liste, taille, cpt):

    if cpt == taille:
        if est_solution (liste):
            liste.append (liste)
            return liste

    else:
        for nb in range (1, somme + 1):
            quadruplet[cpt] = nb

            if element_valide (liste, cpt):
                return ajout_possible (liste, taille, cpt + 1)
        
        quadruplet[cpt] = -1


def ajout (taille, s):

    somme = s
    return ajout_possible ([0] * taille, taille, 0)


while ajout (3, 9) != None:

    print (ajout (3, 9))