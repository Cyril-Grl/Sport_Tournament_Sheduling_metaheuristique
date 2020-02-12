import random

from src.outils import *


def recherche_locale_tabou(matrice, n, fitness, fnc_matrice_inco, fnc_nb_inco, fnc_voisin, nb_turns=0):
    if nb_turns == 0:
        nb_turns = n * n
    nb_inco = fnc_nb_inco(matrice, n)
    liste_pivots = []
    t = 0
    fitness.append(nb_inco)
    while nb_inco != 0 and t < nb_turns:
        t += 1
        matrice_inco = fnc_matrice_inco(matrice, n)
        inco_pivots = [[(i, j), x] for i, ligne in enumerate(matrice_inco) for j, x in enumerate(ligne)]  # if x > 0]
        inco_pivots.sort(key=lambda e: e[1], reverse=True)
        pivots, inco = transpose(inco_pivots)
        if len(liste_pivots) > 20:
            indice = 0
            while pivots[indice] in liste_pivots[-5:]:
                indice += 1
        else:
            indice = random.choice(range(3))
        pivot = pivots[indice]
        liste_pivots.append(pivot)
        vois = fnc_voisin(matrice, pivot)
        inco_voisins = [[v[0], fnc_nb_inco(v[0], n), v[1]] for v in vois]
        inco_voisins.sort(key=lambda e: e[1])
        if inco_voisins[0][1] == 0:
            matrice, nb_inco, piv = inco_voisins[0]
        else:
            matrice, nb_inco, piv = inco_voisins[random.choices([0, 1, 2], [0.85, 0.1, 0.05])[0]]
        liste_pivots.append(piv)
        fitness.append(nb_inco)
    return matrice, t, nb_inco


def recherche_locale(matrice, n, fitness, fnc_matrice_inco, fnc_nb_inco, fnc_voisin, nb_turns=0):
    if nb_turns == 0:
        nb_turns = n * n
    nb_inco = fnc_nb_inco(matrice, n)
    t = 0
    fitness.append(nb_inco)
    while nb_inco != 0 and t < nb_turns:
        t += 1
        matrice_inco = fnc_matrice_inco(matrice, n)
        inco_pivots = [[(i, j), x] for i, ligne in enumerate(matrice_inco) for j, x in enumerate(ligne)]  # if x > 0]
        inco_pivots.sort(key=lambda e: e[1], reverse=True)
        pivots, inco = transpose(inco_pivots)
        indice = random.choice([0, 1, 2])
        pivot = pivots[indice]
        vois = fnc_voisin(matrice, pivot)
        inco_voisins = [[v[0], fnc_nb_inco(v[0], n), v[1]] for v in vois]
        inco_voisins.sort(key=lambda e: e[1])
        if inco_voisins[0][1] == 0:
            matrice, nb_inco, _ = inco_voisins[0]
        else:
            matrice, nb_inco, _ = inco_voisins[random.choices([0, 1, 2], [0.85, 0.1, 0.05])[0]]
        fitness.append(nb_inco)
    return matrice, t, nb_inco
