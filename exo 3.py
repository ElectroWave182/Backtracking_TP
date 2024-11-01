def est_solution (grille):
    
    return True


def ajout_possible (case, grille):

    val = grille[case]
    grille[case] = 0

    N = 81
    lig = case // 9
    col = case % 9
    region = 3 * (lig // 3) + (col // 3)
    haut_gauche = 27 * (region // 3) + 3 * (region % 3)

    liste_lig = grille[9 * lig : 9 * lig + 9]
    liste_col = grille[col : 9 * col : 9]
    liste_carre = grille[haut_gauche : haut_gauche + 2]
    for _ in range(2):
        haut_gauche += 9
        liste_carre += grille[haut_gauche : haut_gauche + 2]
    
    possible = not(val in liste_lig or val in liste_col or val in liste_carre)
    grille[case] = val
    return possible


def afficher (grille):

    for ele in grille:
        print(ele)


def sudoku (case, grille):

    N = 81
    lig = case // 9
    col = case % 9

    

    if case == N:
        if est_solution (grille[:]):
            afficher (grille)
    
    elif grille[case] == 0:
        for val in range (1, 10):
            grille[case] = val
            if ajout_possible (case, grille):
                sudoku (case + 1, grille)

            grille[case] = 0

    else:
        sudoku (case + 1, grille)


grille = [0, 8, 7, 0, 0, 0, 5, 2, 0,
9, 1, 0, 5, 0, 2, 0, 4, 6,
2, 0, 0, 0, 0, 0, 0, 0, 7,
0, 9, 0, 0, 2, 0, 0, 1, 0,
0, 0, 0, 1, 0, 6, 0, 0, 0,
0, 4, 0, 0, 9, 0, 0, 8, 0,
6, 0, 0, 0, 0, 0, 0, 0, 3,
5, 7, 0, 3, 0, 1, 0, 6, 8,
0, 3, 8, 0, 0, 0, 9, 5, 0]


sudoku (0, grille)