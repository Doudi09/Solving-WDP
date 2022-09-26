from GA.Individual import Individual
import random


class Population:
    """ a lsit of Individuals and th elenght """
    #taille de population = size
    #la taille d'un individu = lenght

    def __init__(self, lenght, size, bench):
        self.population = []
        self.size = size
        self.bench = bench
        self.lenght = lenght
        for i in range(0, self.size):
            self.population.append(Individual(lenght, bench))
            # self.population[i].show()
        print('the population has been created')

    def show(self):
        for w in self.population:
            w.show()

    def sort(self):
        print("the sort method")
        self.population.sort(key=lambda x: x.fitness, reverse=True)

    def mutation_non_binary(self, mutation_rate):
        for w in range(2, self.size):
            self.population[w].mutation(mutation_rate, self.bench)


    def crossover_non_binary_migration(self):
        new_population = []
        # keeping the best to the population to the next generation :
        new_population.append(self.population[0])
        # print("the 0 new  >>")
        # new_population[0].show()
        # print("the 0 >>")
        # self.population[0].show()
        for w in range(0, self.size - 3,3):
            if w % 2 == 0:
                new_population.append(
                    self.population[w].crossover(self.population[w + 1], self.bench))
            else:
                new_population.append(Individual(self.lenght, self.bench))
        # completing the rest of th enew population randomly :
        while (len(new_population) != self.size):
            new_population.append(Individual(self.lenght, self.bench))
        # print("the new population after croosover ")
        # print(new_population)
        self.population = new_population.copy()




    def crossover_non_binary(self):
        new_population = []
        # keeping the best to the population to the next generation :
        new_population.append(self.population[0])
        # print("the 0 new  >>")
        # new_population[0].show()
        # print("the 0 >>")
        # self.population[0].show()
        for w in range(0, self.size - 1):
            new_population.append(
                self.population[w].crossover(self.population[w + 1], self.bench))
        # completing the rest of th enew population randomly :
        while (len(new_population) != self.size):
            new_population.append(Individual(self.lenght, self.bench))
        # print("the new population after croosover ")
        # print(new_population)
        self.population = new_population.copy()

    # mutation :
    # idk why but i think that its gnonna be hard :(
    def mutation(self, mutation_rate):
        # we keep the best solution found
        print("the 0 >> mutation ==============================")
        self.population[0].show()
        for w in range(2, self.size):
            # selecting randomly ...
            # print("the mutaed element :")
            self.population[w].mutation(mutation_rate, self.bench)

    # selection :
    def selction(self):
        # we select the parents pool
        parents = self.population[1:self.size / 2]

    # crossover :

    def crossover(self, crossover_point):
        new_population = []
        # keeping the best to the population to the next generation :
        new_population.append(self.population[0])
        # print("the 0 new  >>")
        # new_population[0].show()
        # print("the 0 >>")
        # self.population[0].show()
        for w in range(0, self.size - 1):
            new_population.append(
                self.population.__getitem__(w).crossover(self.population.__getitem__(w + 1), crossover_point,
                                                         self.bench))
        # completing the rest of th enew population randomly :
        while (len(new_population) != self.size):
            new_population.append(Individual(self.lenght, self.bench))
        # print("the new population after croosover ")
        # print(new_population)
        self.population = new_population.copy()
