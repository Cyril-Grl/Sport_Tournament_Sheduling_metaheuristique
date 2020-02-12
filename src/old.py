# OLD a trier


# def main1(n):
#     import matplotlib.pyplot as plt
#     import numpy as np
#     import seaborn as sns
#
#     sns.set(style="darkgrid")
#     lf = len(fitness)
#     t = np.arange(0, lf, 1)
#     plt.plot(t, fitness, color='b', label='recherche totale')
#     plt.legend()
#     if nombre_incoherences_totales(m, n) == 0:
#         plt.title('Recherche ok')
#     else:
#         plt.title('Recherche pas ok')
#     plt.show()

# from algo_gen.tools.plot import show_stats
# show_stats(population.stats)

# if __name__ == '__main__':
#     import time
#
#     start_time = time.time()
#     # main1(12)
#     s = 0
#     for i in range(1000):
#         random.seed(i)
#         s += recherche_locale_init(10)
#     print(f's = {s}')
#     print("--- %s seconds ---" % (time.time() - start_time))


# def main(n):
#     # random.seed(9)
#
#     n, s, p, r = conditions(n)
#     affiche_conditions(n, s, p, r)
#
#     random.shuffle(r)
#     m = r_to_m(r, s, p)
#     # nb_inco_s = nombre_incoherences_semaine(m, n)
#     # nb_inco_p = nombre_incoherences_periodes(transpose(m), n)
#     # print("Planning debut de recherche :")
#     # pprint(m)
#     # print(f'Incoherances semaines : {nb_inco_s}')
#     # pprint(matrice_incoherences_semaine(m, n), width=(len(m[0]) * 4))
#     # print(f'Incoherances periodes : {nb_inco_p}')
#     # pprint(matrice_incoherences_periode(transpose(m), n), width=(len(m) * 4))
#     # print(f'Incoherances totales : {nombre_incoherences_totales(m, n)}')
#     # pprint(matrice_incoherences_totales(m, n), width=(len(m[0]) * 4))
#     nb_iterations = 0
#
#     fitness = []
#     m, t, nb_inco_t = recherche_locale_tabou(m, n, fitness, matrice_incoherences_totales, nombre_incoherences_totales,
#                                              voisins_totaux, n * 30)
#     nb_iterations += t
#     print(f'reste {nb_inco_t} incoherences')
#     fitness1 = []
#     m, t, nb_inco_t = recherche_locale_tabou(m, n, fitness1, matrice_incoherences_semaine, nombre_incoherences_semaine,
#                                              voisins_totaux, n * 100)
#     nb_iterations += t
#     print(
#             f'contrainte semaine resolue en {nb_iterations} tours (inco semaine : {nombre_incoherences_semaine(m, n)}, inco periode : {nombre_incoherences_periodes(transpose(m), n)})')
#
#     # for l in m:
#     #     random.shuffle(l)
#     fitness2 = []
#     # m, t, nb_inco_t = recherche_locale_tabou(m, n, fitness2, matrice_incoherences_totales, nombre_incoherences_totales,
#     #                                          voisins_totaux, n * 50)
#     nb_iterations += t
#     fitness3 = []
#     # for l in m:
#     #     random.shuffle(l)
#     m_t, t, nb_inco_t = recherche_locale_tabou(transpose(m), n, fitness3, matrice_incoherences_periode,
#                                                nombre_incoherences_periodes,
#                                                voisins_colonne, n * 100)
#     nb_iterations += t
#     m = transpose(m_t)
#
#     nb_inco_s = nombre_incoherences_semaine(m, n)
#     nb_inco_p = nombre_incoherences_periodes(transpose(m), n)
#     print(f'Incoherances semaines : {nb_inco_s}')
#     print(f'Incoherances periodes : {nb_inco_p}')
#     # nb_inco_s = nombre_incoherences_semaine(m, n)
#     # nb_inco_p = nombre_incoherences_periodes(transpose(m), n)
#     # print(f'salut {nb_inco_p} {nb_inco_s} {nb_inco_t} t {t}')
#     # while (nb_inco_p != 0) and (nb_inco_s != 0) and (nb_iterations < n ^ 8):
#     #     # print("!"*80)
#     #     # print(f'coucou {nb_inco_p} {nb_inco_s} {nb_inco_p != 0 or nb_inco_s != 0}')
#     #     if nb_inco_s != 0:
#     #         m, t, nb_inco_s = recherche_locale(m, n, fitness, matrice_incoherences_semaine,
#     #                                            nombre_incoherences_semaine, voisins_colonne)
#     #         # print(f'semaines : t {t} nb_inco {nb_inco_s}')
#     #         nb_iterations += t
#     #         # print(f'nb_inco_s {nb_inco_s}')
#     #
#     #     nb_inco_p = nombre_incoherences_periodes(transpose(m), n)
#     #     if nb_inco_p != 0:
#     #         m_t = transpose(m)
#     #         m_t, t, nb_inco_p = recherche_locale(m_t, n, fitness, matrice_incoherences_periode,
#     #                                              nombre_incoherences_periodes, voisins_colonne)
#     #         # print(f'periodes : t {t} nb_inco {nb_inco_p}')
#     #         nb_iterations += t
#     #         # print(f'nb_inco_p {nb_inco_p}')
#     #         m = transpose(m_t)
#     #     nb_inco_s = nombre_incoherences_semaine(m, n)
#     # print(f'nb_inco_s {nb_inco_s}')
#
#     # nb_inco_t = nombre_incoherences_totales(m, n)
#     # while nb_inco_t != 0:
#     #     # m, t, nb_inco_s = recherche_locale(m, n, matrice_incoherences_semaine, nombre_incoherences_semaine, voisins_proches)
#     #     # nb_iterations += t
#     #     m, t, nb_inco_t = recherche_locale(m, n, matrice_incoherences_totales, nombre_incoherences_totales, voisins_totaux)
#     #     nb_iterations += t
#     #     print(f'nb_inco_t {nb_inco_t}')
#     print(f'nb iterations : {nb_iterations}')
#
#     print("Résultat : ")
#     pprint(m)
#
#     print(f'nombre_incoherences_semaine : {nombre_incoherences_semaine(m, n)}')
#
#     print(semaines_ok(m, n))
#
#     print(f'nombre_incoherences_periodes : {nombre_incoherences_periodes(transpose(m), n)}')
#     import matplotlib.pyplot as plt
#     import numpy as np
#     import seaborn as sns
#
#     sns.set(style="darkgrid")
#     lf = len(fitness)
#     lf1 = len(fitness1)
#     lf2 = len(fitness2)
#     lf3 = len(fitness3)
#     t = np.arange(0, lf, 1)
#     t1 = np.arange(lf, lf + lf1, 1)
#     t2 = np.arange(lf + lf1, lf + lf1 + lf2, 1)
#     t3 = np.arange(lf + lf1 + lf2, lf + lf1 + lf2 + lf3, 1)
#     plt.plot(t, fitness, color='b', label='recherche totale')
#     plt.plot(t1, fitness1, color='r', label='recherche semaines')
#     plt.plot(t2, fitness2, color='g', label='recherche totale')
#     plt.plot(t3, fitness3, color='y', label='recherche periodes')
#     plt.legend()
#     if nombre_incoherences_totales(m, n) == 0:
#         plt.title('Recherche ok')
#         plt.show()
#         return 1
#     else:
#         plt.title('Recherche pas ok')
#         plt.show()
#         return 0

# if __name__ == '__main__':
#     import time
#     import random
#     from src.init_recherche import init_algo_gen
#
#     print('memetique modif')
#     stats = {}
#     for n in range(14, 20, 2):
#         start_time = time.time()
#         s = 0
#         for i in range(2, 11):
#             random.seed(i)
#             score, fitness = init_algo_gen(n)
#             s += score
#             stats[f'{n}_{i}'] = fitness
#
#         print(f'n = {n}')
#         print(f's = {s}')
#         print(f't = {time.time() - start_time} s')
#         if s == 0:
#             import json
#
#             with open('memetique_modif_2_10.json', 'w') as fp:
#                 json.dump(stats, fp)
#             exit(0)


# m = r_to_m(r, s, p)
# print(nombre_incoherences_semaine(m,n))
# pprint(m)
# pprint(matrice_incoherences_semaine(m, n))
# voisins = voisins_semaine(m, ((1,1)))
# for v in voisins:
#     pprint(v)


# while nb_inco_p != 0 or nb_inco_s != 0:
#     while nb_inco_s != 0 and t < (n * n):
#         nb_iterations += 1
#         t += 1
#         # for t in range(10):
#         # print(f'tour {t} - incoherences semaines : {nb_inco_s}')
#         matrice_inco_s = matrice_incoherences_semaine(m, n)
#         inco_pivots = [[(i, j), x] for i, semaine in enumerate(matrice_inco_s)
#                        for j, x in enumerate(semaine) if x > 0]
#         inco_pivots.sort(key=lambda e: e[1], reverse=True)
#         pivots, inco = transpose(inco_pivots)
#         if len(liste_pivots) > 10:
#             indice = 0
#             while pivots[indice] in liste_pivots[-(len(inco) - 1):]:
#                 indice += 1
#         else:
#             indice = random.choice(range(3))
#         pivot = pivots[indice]
#         liste_pivots.append(pivot)
#         vois = voisins(m, pivot)
#         inco_voisins = [[v, nombre_incoherences_semaine(v, n)]
#                         for v in vois]
#         inco_voisins.sort(key=lambda e: e[1])
#         m, nb_inco_s = inco_voisins[random.choices([0, 1], [0.8, 0.2])[0]]
#     # print(f'incoherences semaines : {nb_inco_s}')
#     m_t = transpose(m)
#     if t == 0:
#         random.shuffle(m_t[random.randint(0, len(m_t) - 1)])
#     nb_inco_p = nombre_incoherences_periodes(m_t, n)
#     liste_pivots = []
#     t = 0
#     while nb_inco_p != 0 and t < (n * n):
#         nb_iterations += 1
#         t += 1
#         # for t in range(10):
#         # print(f'tour {t} - incoherences periodes : {nb_inco_p}')
#         matrice_inco_p = matrice_incoherences_periode(m_t, n)
#         inco_pivots = [[(i, j), x] for i, periode in enumerate(matrice_inco_p)
#                        for j, x in enumerate(periode) if x > 0]
#         inco_pivots.sort(key=lambda e: e[1], reverse=True)
#         pivots, inco = transpose(inco_pivots)
#         if len(liste_pivots) > 10:
#             indice = 0
#             while pivots[indice] in liste_pivots[-(len(inco) - 1):]:
#                 indice += 1
#         else:
#             indice = random.choice(range(3))
#         pivot = pivots[indice]
#         liste_pivots.append(pivot)
#         vois = voisins(m_t, pivot)
#         inco_voisins = [[v, nombre_incoherences_periodes(v, n)]
#                         for v in vois]
#         inco_voisins.sort(key=lambda e: e[1])
#         m_t, nb_inco_p = inco_voisins[random.choices([0, 1], [0.8, 0.2])[0]]
#     # print(f'incoherences periodes : {nb_inco_p}')
#     m = transpose(m_t)
#     if t == 0:
#         random.shuffle(m[random.randint(0, len(m) - 1)])
#     nb_inco_s = nombre_incoherences_semaine(m, n)
#     liste_pivots = []
#     t = 0

# import matplotlib.pyplot as plt
#
#
# def show_stats(stats, title=None):
#     fig, ax = plt.subplots(figsize=(8, 8))
#
#     if title:
#         plt.title(title)
#     plt.xlabel("tours")
#     plt.ylabel('fitness')
#     # plt.xlim(0, len(stats['max_fitness']))
#     # plt.ylim(-70, 0)  # (-70,0)#(0, 100)  # stats['parameters']['chromosome size'])  # stats['max_fitness'][-1]*1.1
#
#     ax.plot(stats['max_fitness'], color='red', label='max')
#     ax.plot(stats['min_fitness'], color='green', label='min')
#     ax.plot(stats['mean_fitness'], color='blue', label='mean')
#     # ax.plot(stats['fitness_diversity'], color='black', label='fitness_diversity')
#
#     windows_size = 49
#     polynomial_order = 3
#
#     # ax.plot(savgol_filter(stats['max_fitness'], windows_size, polynomial_order), color='red', linestyle='dashed',
#     #         label='max_fitness soft')
#     # ax.plot(savgol_filter(stats['min_fitness'], windows_size, polynomial_order), color='green', linestyle='dashed',
#     #         label='min_fitness soft')
#     # ax.plot(savgol_filter(stats['mean_fitness'], windows_size, polynomial_order), color='blue', linestyle='dashed',
#     #         label='mean_fitness soft')
#
#     plt.legend(title='fitness', loc='lower right')
#
#     # plt.title("\n".join(textwrap.wrap(str(stats['parameters']['mutation'][1]), 120)))
#     plt.show()
#
#     # fig, ax = plt.subplots(figsize=(10, 10))
#     #
#     # ax.plot(stats['diversity'], color='yellow', label='diversity')
#     # ax.plot(stats['max_age'], color='c', label='max_age')
#     # ax.plot(stats['mean_age'], color='m', label='mean_age')
#     #
#     # plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
#     #
#     # plt.show()
#     #
#     # fig, ax = plt.subplots(figsize=(10, 10))
#     #
#     # ax.plot(stats['total_fitness'], color='black', label='total_fitness')
#     #
#     # plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
#     #
#     # plt.show()


# m = r_to_m(r, s, p)
# m_t = transpose(m)
# print(nombre_incoherences_periodes(m_t, n))
# pprint(m_t)
# pprint(matrice_incoherences_periode(m_t, n))
# voisins = voisins_periode(m_t, ((1, 1)))
# for v in voisins:
#     pprint(v)


# print("Semaines :")
# # for i in range(s):
# #     print(f's{i} : {r[i*p:i*p+p]}')
# # print("Périodes :")
# # for i in range(p):
# #     print(f'p{i} : {r[i::p]}')


# ##############################
# #          semaines          #
# ##############################

# def semaine_ok(semaine, n):
#     present = [False] * n
#     for a, b in semaine:
#         if present[a] or present[b]:
#             return False
#         present[a] = True
#         present[b] = True
#     return True


# def semaines_ok(m, n):
#     for semaine in m:
#         if not semaine_ok(semaine, n):
#             return False
#     return True


# def nombre_incoherences_semaine(m, n):
#     nb = 0
#     for semaine in m:
#         present = [-1] * n
#         for a, b in semaine:
#             present[a] += 1
#             present[b] += 1
#         nb += sum([abs(ab) for ab in present])
#     return nb


# def liste_incoherences_semaine(m, n, liste_incoherences):
#     p = len(m[0])
#     for i, semaine in enumerate(m):
#         present = [-1] * n
#         for a, b in semaine:
#             present[a] += 1
#             present[b] += 1
#         inco = list(map(abs, present))
#         for j, ab in enumerate(semaine):
#             a, b = ab
#             liste_incoherences[i * p + j] += (inco[a] > 0) + (inco[b] > 0)


# def voisins_semaine(r, s, p, pivot):
#     voisins = []
#     for i in range(pivot % s, s * p, p):
#         if i != pivot:
#             v = copy.deepcopy(r)
#             permutation(v, i, pivot)
#             voisins.append(v)
#     return voisins


# def voisins_semaine_matrice(m, pivot):
#     voisins = []
#     for i in len(m):
#         if i != pivot[0]:
#             v = copy.deepcopy(m)
#             permutation_m(v,pivot,(i, pivot[1]))
#             voisins.append(v)
#     return voisins


# def matrice_incoherences_semaine(m, n, matrice_incoherences):
#     # matrice_inco_s = [[0] * p for _ in range(s)]
#     for num_s, semaine in enumerate(m):
#         present = [-1] * n
#         for a, b in semaine:
#             present[a] += 1
#             present[b] += 1
#         inco = list(map(abs, present))
#         for num_p, ab in enumerate(semaine):
#             a, b = ab
#             matrice_incoherences[num_s][num_p] += (inco[a] > 0) + (inco[b] > 0)

# # matrice_inco_s = [[0] * p for _ in range(s)]
# # pprint(matrice_inco_s)
# # m = r_to_m(r, s, p)
# # matrice_incoherences_periode(transpose(m), n, matrice_inco_s)
# # pprint(m)
# # pprint(matrice_inco_s)

# ##############################
# #          periodes          #
# ##############################

# def periode_ok(semaine, n):
#     present = [0] * n
#     for a, b in semaine:
#         present[a] += 1
#         present[b] += 1
#         if present[a] > 2 or present[b] > 2:
#             return False
#     return True


# def periodes_ok(m_t, n):
#     for periode in m_t:
#         if not periode_ok(periode, n):
#             return False
#     return True


# def nombre_incoherences_periode(periode, n):
#     present = [0] * n
#     for a, b in periode:
#         present[a] += 1
#         present[b] += 1
#     return sum([0 if i <= 2 else i - 2 for i in present])


# def nombre_incoherences_periodes(m_t, n):
#     nb = 0
#     for periode in m_t:
#         present = [0] * n
#         for a, b in periode:
#             present[a] += 1
#             present[b] += 1
#         nb += sum([0 if i <= 2 else i - 2 for i in present])
#     return nb


# def liste_incoherences_periode(m_t, s, p, n, liste_incoherences):
#     for j, periode in enumerate(m_t):
#         present = [0] * n
#         for a, b in periode:
#             present[a] += 1
#             present[b] += 1
#         inco = [0 if v <= 2 else v - 2 for v in present]
#         for i, ab in enumerate(periode):
#             a, b = ab
#             liste_incoherences[i * p + j] += (inco[a] > 0) + (inco[b] > 0)


# def voisins_periode(r, s, p, pivot):
#     voisins = []
#     for i in range(pivot % p, p):
#         e = i + (pivot // p) * p
#         if e != pivot:
#             v = copy.deepcopy(r)
#             permutation(v, e, pivot)
#             voisins.append(v)
#     return voisins

# def voisins_periode_matrice(m_t, pivot):
#     voisins = []
#     for i, periode in enumerate(m_t):
#         if i != pivot[1]:
#             v = copy.deepcopy(m_t)
#             permutation_m(v, pivot, (i,pivot[1]))
#             voisins.append(v)
#     return voisins

# # m = r_to_m(r,s,p)
# # m_t = transpose(m)
# # voisins = voisins_periode_matrice(m_t, (1,1))
# # pprint(m_t)
# # print()
# # for v in voisins:
# #     pprint(v)

# def matrice_incoherences_periode(m_t, n, matrice_incoherences):
#     # matrice_inco_s = [[0] * p for _ in range(s)]
#     # la matrice est transposee compare avec celle de semaines
#     for num_p, periode in enumerate(m_t):
#         present = [0] * n
#         for a, b in periode:
#             present[a] += 1
#             present[b] += 1
#         inco = [0 if v <= 2 else v - 2 for v in present]
#         for num_s, ab in enumerate(periode):
#             a, b = ab
#             matrice_incoherences[num_s][num_p] += (inco[a] > 0) + (inco[b] > 0)


# ##############################
# #           totales          #
# ##############################


# def voisins(r, s, p, pivot):
#     voisins = []
#     for i in range(s * p):
#         if i != pivot:
#             v = copy.deepcopy(r)
#             permutation(v, i, pivot)
#             voisins.append(v)
#     return voisins


# len(voisins(r, s, p, 5))


# random.shuffle(r)
# nb_inco_s = sum([nombre_incoherences_semaine(r[i * p:i * p + p], n) for i in range(s)])
# i = 0
# while nb_inco_s > 0:
#     i += 1
#     if i > 100:
#         break
#     print(f'tour {i} - incoherences semaine : {nb_inco_s}')
#     l_inco_s = [0] * len(r)
#     m = r_to_m(r, s, p)
#     liste_incoherences_semaine(m, s, p, n, l_inco_s)
#     maximum = max(l_inco_s)
#     indices = [i for i, x in enumerate(l_inco_s) if x == maximum]
#     pivot = random.choice(indices)
#     voisins_s = voisins_semaine(r,s,p,pivot)
#     l_nb_inco_v_s = [(v, sum([nombre_incoherences_semaine(
#     r[i * p:i * p + p], n) for i in range(s)])) for v in voisins_s]
#     l_nb_inco_v_s.sort(key=lambda e: e[1])
#     r, nb_inco_s = random.choice(l_nb_inco_v_s[:2])

# print_matrix_inco(r, l_inco_s, s, p)


# def select(l_inco_voisins):
#     return random.choice(l_inco_voisins[:1])


# random.shuffle(r)
# inco_tot = nombre_incoherences_totales(r, s, p, n)
# for t in range(1000):
#     print(f'tour {t} - incoherences : {inco_tot}')
#     liste_incoherences = liste_incoherences_totales(r, s, p, n)
#     if inco_tot <= 2:
#         print_matrix_inco(r, liste_incoherences, s, p)
#     badest = liste_incoherences.index(max(liste_incoherences))
#     vois = voisins(r, s, p, badest)
#     l_inco_voisins = []
#     for v in vois:
#         l_inco_voisins.append((v, nombre_incoherences_totales(v, s, p, n)))
#     l_inco_voisins.sort(key=lambda e: e[1])
#     r, inco_tot = select(l_inco_voisins)
# print_matrix_inco(r, liste_incoherences, s, p)
# #     r = vois[l_inco_voisins.index(min(l_inco_voisins))]

# def remplir_planning(matchs, n):
#     print(matchs)
#     i = 0
#     planning = []
#     while matchs != []:
#         print("matchs")
#         pprint(matchs)
#         print("planning")
#         pprint(planning)
#         semaine = []
#         valide = -1
#         while valide != 1:
#             print(semaine)
#             semaine.append(matchs[i])
#             valide = semaine_ok(semaine, n)
#             if valide >=0:
#                 matchs.pop(i)
#             else:
#                 semaine = semaine[0:-1]
#             i = (i+1)%len(matchs)
#         planning.append(semaine)
# remplir_planning(r, n)
# def incoherances(r, s, p, n):
#     liste_incoherences = [0] * len(r)
#     for i in range(s):
#         present = [0] * n
#         for a,b in r[i*p:i*p+p]:
#             present[a] += 1
#             present[b] += 1
#         print("present s")
#         print(present)
#         inco = [abs(i-1) for i in present]
#         print("inco s")
#         print(inco)
#         for j,m in enumerate(r[i*p:i*p+p]):
#             a,b = m
#             liste_incoherences[i*p+j] += inco[a] + inco[b]
#     for i in range(p):
#         present = [0] * n
#         for a, b in r[i::p]:
#             present[a] += 1
#             present[b] += 1
#         print("present p")
#         print(present)
#         inco = [0 if i <= 2 else i-2 for i in present]
#         print("inco p")
#         print(inco)
#         for j,m in enumerate(r[i::p]):
#             a,b = m
#             liste_incoherences[j*p+i] += inco[a] + inco[b]
#     for i in range(s):
#         for j in range(p):
#             print(liste_incoherences[i*p+j], end=" ")
#         print()
#     print(liste_incoherences)
#     print(f'sum inco {sum(liste_incoherences)}')
# incoherances(r,s,p,n)

# def nombre_incoherences_totales(r, s, p, n):
#     m = r_to_m(r,s,p)
#     nb_inco_semaine = nombre_incoherences_semaine(m, s, p, n)
#     inco_semaines = sum(
#         [nombre_incoherences_semaine(r[i * p:i * p + p], n) for i in range(s)])
#     inco_periodes = sum([nombre_incoherences_periode(r[i::p], n) for i in range(p)])
#     return inco_semaines + inco_periodes


# def liste_incoherences_totales(r, s, p, n):
#     liste_incoherences = [0] * len(r)
#     m = r_to_m(r, s, p)
#     liste_incoherences_semaine(m, s, p, n, liste_incoherences)
#     m_t = list(map(list, zip(*m)))
#     liste_incoherences_periode(m_t, s, p, n, liste_incoherences)
#     return liste_incoherences


# def print_matrix_inco(m, inco, s, p):
#     for i in range(s):
#         for j in range(p):
#             print(f'{m[i*p+j]}->{inco[i*p+j]}', end=' ')
#         print()


# # liste_incoherences = liste_incoherences_totales(r, s, p, n)
# # print_matrix_inco(r, liste_incoherences, s, p)
# # print(f'Nombre d\'incoherences : {nombre_incoherences_totales(r,s,p,n)}')
