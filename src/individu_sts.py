from pprint import pformat

from algo_gen.classes import IndividualPermutation

from src.recherche_locale import *


class IndividualSTS(IndividualPermutation):

    def __init__(self, parameters, empty=False):
        super().__init__(parameters, empty=empty)
        if parameters['number of team'] % 2 != 0:
            print("Error, the number of team must be a pair number")
            exit(1)
        self.n = parameters['number of team']
        self.s = self.n - 1
        self.p = self.n // 2
        if empty:
            self.sequence = [None] * (self.s * self.p)
        else:
            self.sequence = [(i, j) for i in range(0, self.n) for j in range(i, self.n) if i != j]
            random.shuffle(self.sequence)

    def improve(self):
        m = r_to_m(self.sequence, self.s, self.p)
        m, _, _ = recherche_locale(m, self.n, matrice_incoherences_totales, nombre_incoherences_totales, voisins_totaux,
                                   10)
        self.sequence = m_to_r(m)

    def fitness(self):
        m = r_to_m(self.sequence, self.s, self.p)
        if self.parameters['only weeks']:
            return - nombre_incoherences_semaine(m, self.n)
        else:
            return - nombre_incoherences_totales(m, self.n)

    def crossover(self, other):
        return IndividualSTS(self.parameters), IndividualSTS(self.parameters)

    def mutate(self):
        if random.random() <= self.parameters['proportion mutation']:
            if self.parameters['methode'] == 'AG':
                method = random.choices(['insert', 'swap'], [0.5, 0.5])[0]
            elif self.parameters['methode'] == 'AM':
                method = 'local_search'
            elif self.parameters['methode'] == 'AMM':
                method = random.choices(['insert', 'swap', 'local_search'], [0.475, 0.475, 0.05])[0]
            else:
                print('erreur methode algo genetique/memetique')
                method = random.choices(['insert', 'swap'], [0.5, 0.5])[0]
            if method == 'insert':
                # print('insert')
                length = len(self.sequence)
                rand1 = random.randint(0, length - 3)
                rand2 = random.randint(rand1 + 1, length - 1)
                self[rand1 + 1], self[rand2] = self[rand2], self[rand1 + 1]
            elif method == 'swap':
                # print('swap')
                length = len(self.sequence)
                rand1 = random.randint(0, length - 3)
                rand2 = random.randint(rand1 + 1, length - 1)
                self[rand1], self[rand2] = self[rand2], self[rand1]
            elif method == 'local_search':
                # print('local_search')
                m = r_to_m(self.sequence, self.s, self.p)
                m, _, _ = recherche_locale_tabou(m, self.n, [], matrice_incoherences_totales,
                                                 nombre_incoherences_totales,
                                                 voisins_totaux, self.n * 20)
                self.sequence = m_to_r(m)

    def basic_order(self):
        return [(i, j) for i in range(0, self.parameters['number of team']) for j in
                range(i, self.parameters['number of team']) if i != j]

    def __eq__(self, other):
        if type(other) != type(self):
            return False
        for a, b in zip(self.sequence, other.sequence):
            if a != b:
                return False
        return True

    def __repr__(self):
        r = ""
        s = self.parameters['number of team'] - 1
        p = self.parameters['number of team'] // 2
        m = [self.sequence[i * p:i * p + p] for i in range(s)]
        r += pformat(m, indent=1)
        r += f" {self.fitness()}"
        return r

    def __hash__(self):
        r = ""
        for g in self.sequence:
            r += str(g[0]) + str(g[1])
        return int(r, 10)
