# this exercise was done in class

import random


class Gene:
    def __init__(self):
        self.state = random.randint(0, 1)

    def flip(self):
        self.state = 0 if self.state == 1 else 1

    def __repr__(self):
        return f'{self.state}'


class Chromosome:
    def __init__(self):
        self.genes = [Gene() for i in range(0, 10)]
        print('created 10 genes')
        print(self.genes)

    def mutate(self):
        indexes = list(range(0, len(self.genes)))
        random.shuffle(indexes)
        print('shuffled indexes', indexes)
        index_sub_selection = indexes[0:random.choice(indexes)]
        print('the shuffled subselection', index_sub_selection)
        for idx in index_sub_selection:
            print('looping over gene', idx)

            if random.randint(0, 1):
                self.genes[idx].flip()
                print('i flipped', self.genes[idx])
            else:
                print('i didn\'t flip')


class DNA:
    def __init__(self):
        self.chromosomes = [Chromosome() for i in range(10)]

    def mutate(self):
        selected_chromosomes = random.sample(
            self.chromosomes, random.randint(0, len(self.chromosomes)))
        for chromo in selected_chromosomes:
            if random.randint(0, 1):
                chromo.mutate()
                print('i mutated', chromo)
            else:
                print('i didn\'t mutate')


# chromo = Chromosome()
# chromo.mutate()
# print(chromo.genes)

