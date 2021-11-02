import random


class Gene():
    genes = []

    def __init__(self, val):
        self.genes.append(val)

    def mutate(self):
        sequence = ''
        for i in range(len(self.genes)):
            self.genes[i] = random.randint(0, 1)
            sequence += str(self.genes[i])
        print(sequence)


class Chromosome(Gene):
    def __init__(self, genes):
        for g in genes:
            super().__init__(g)


class DNA(Chromosome):
    def __init__(self, chromosomes):
        for c in chromosomes:
            super().__init__(c)


class Organism:
    # environment is the percentage number
    # to be in the range of a random number from 0 -100
    def __init__(self, dna, environment):
        ran = random.randint(0, 100)
        if ran <= environment:
            dna.mutate()

# generates random dna sequence


def DNA_generator():
    dna = []
    for c in range(10):
        # creating a single chromosom
        chromosome = []
        for j in range(10):

            gene = Gene(random.randint(0, 1))
            chromosome.append(gene)

        dna.append(chromosome)
    return DNA(dna)


yeast_dna = DNA_generator()
print(yeast_dna.genes)

# algae = DNA_generator()
# protozoa = DNA_generator()

# yeast = Organism(yeast_dna, 20)
# algae = Organism(algae, 45)
# protozoa = Organism(protozoa, 90)


# # generates random dna sequence
# def DNA_generator():
#     chromosomes = []
#     # create 10 chromosome for dna
#     for c in range(10):
#         genes = []
#         # create 10 genes for each chromosome
#         for g in range(10):
#             gene = Gene(random.randint(0, 1))
#             genes.append(gene)
#         chromosomes.append(Chromosome(genes))
#     return DNA(chromosomes)
