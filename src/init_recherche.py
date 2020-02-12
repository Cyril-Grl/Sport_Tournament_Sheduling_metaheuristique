import random

from src.outils import *
from src.recherche_locale import recherche_locale, recherche_locale_tabou


def recherche_locale_tabou_modif_init(n):
    n, s, p, r = conditions(n)
    random.shuffle(r)
    m = r_to_m(r, s, p)
    nb_iterations = 0
    fitness = []
    m, t, nb_inco_t = recherche_locale_tabou(m, n, fitness, matrice_incoherences_totales, nombre_incoherences_totales,
                                             voisins_totaux, n * 100)
    nb_iterations += t
    fitness1 = []
    m, t, nb_inco_t = recherche_locale_tabou(m, n, fitness1, matrice_incoherences_semaine, nombre_incoherences_semaine,
                                             voisins_totaux, n * 100)
    nb_iterations += t
    fitness2 = []
    m_t, t, nb_inco_t = recherche_locale_tabou(transpose(m), n, fitness2, matrice_incoherences_periode,
                                               nombre_incoherences_periodes,
                                               voisins_colonne, n * 100)
    nb_iterations += t
    m = transpose(m_t)

    if nombre_incoherences_totales(m, n) == 0:
        return 1, [fitness, fitness1, fitness2]
    else:
        return 0, [fitness, fitness1, fitness2]


def recherche_locale_init(n):
    n, s, p, r = conditions(n)
    random.shuffle(r)
    m = r_to_m(r, s, p)
    nb_iterations = 0
    fitness = []
    m, t, nb_inco_t = recherche_locale(m, n, fitness, matrice_incoherences_totales, nombre_incoherences_totales,
                                       voisins_totaux, n * 200)
    nb_iterations += t

    if nombre_incoherences_totales(m, n) == 0:
        return 1, fitness
    else:
        return 0, fitness


def recherche_locale_tabou_init(n):
    n, s, p, r = conditions(n)
    random.shuffle(r)
    m = r_to_m(r, s, p)
    nb_iterations = 0
    fitness = []
    m, t, nb_inco_t = recherche_locale_tabou(m, n, fitness, matrice_incoherences_totales, nombre_incoherences_totales,
                                             voisins_totaux, n * 200)
    nb_iterations += t

    if nombre_incoherences_totales(m, n) == 0:
        return 1, fitness
    else:
        return 0, fitness


def launch_algo_gen(n, methode):
    from algo_gen.classes import Population

    from src.individu_sts import IndividualSTS

    def final_condition(pop):
        if pop.stats['max_fitness'][-1] == 0:
            return False
        else:
            return not (pop.nb_turns == pop.parameters['nb turn max'])

    def each_turn(pop):
        if pop.stats["diversity"][-1] < int(pop.parameters["population size"] * 0.4):
            diff_indiv = set([i for i, _, _ in pop.individuals])
            pop.individuals = []
            for indiv in diff_indiv:
                pop.individuals.append((indiv, indiv.fitness(), 0))
            for i in range(len(diff_indiv), pop.parameters["population size"]):
                new_indiv = IndividualSTS(pop.parameters)
                pop.individuals.append((new_indiv, new_indiv.fitness(), 0))

    parametres = {
            'individual'           : IndividualSTS,
            'only weeks'           : False,
            'number of team'       : n,
            'methode'              : methode,

            'population size'      : 100,
            'chromosome size'      : (n - 1) * int(n / 2),

            'termination_condition': final_condition,
            'function_each_turn'   : each_turn,
            'nb turn max'          : 1000,

            'selection'            : ['select_tournament'],
            'proportion selection' : 20,

            'crossover'            : ['pmx'],
            'proportion crossover' : 1,

            'mutation'             : ['individual'],
            'proportion mutation'  : 0.4,

            'insertion'            : 'age',
    }
    population = Population(parametres, description=False)
    population.start()

    fitness = population.stats['max_fitness']
    m = r_to_m(population.individuals[0][0].sequence, n - 1, int(n / 2))
    if nombre_incoherences_totales(m, n) == 0:
        return 1, fitness
    else:
        return 0, fitness


def init_algo_gen(n):
    return launch_algo_gen(n, "AG")


def init_algo_meme(n):
    return launch_algo_gen(n, "AM")


def init_algo_meme_modif(n):
    return launch_algo_gen(n, "AMM")
