global liste
liste = []

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


def ajout_possible (quadruplet, taille, cpt):

    if cpt == 4
        if est_solution (quadruplet):
            print (quadruplet)

    else:
        for nb in range (taille):
            quadruplet[cpt] = nb

            if element_valide (quadruplet, cpt):
                return ajout_possible (quadruplet, taille, cpt + 1)
        
            else:
                quadruplet[cpt] = -1


def ajout (taille):

    return ajout_possible ([-1] * 4, taille, 0)


while len (ajout (4)) != 4:

    print (ajout (4))