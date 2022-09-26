from GA.Population import Population


class GeneticAlgorithm:

    def __init__(self, size, lenght, bench):
        #print('the init function ')
        self.size = size
        self.bench = bench

        self.lenght = lenght
        #print('creating the initial population ....')
        self.population = Population(lenght, size, bench)
        #print('the ga instance has been created ')



    def run_non_binary_miggration(self, maxIteration, mutation_rate):

        #print(self.window.result.toPlainText())
        i = 0
        same_result = 0
        max = 0
        migration = False
        while True:
            self.population.sort()
            #self.window.addTextDetailedExec('the best solution found till now :\n' +
            #                               self.population.population[0].text())
            self.population.population[0].show()
            # the crossover : monopoint
            self.population.crossover_non_binary()
            """
            
            if not migration :
                self.population.crossover_non_binary()
            else:
                self.population.crossover_non_binary_migration()

            """
            # the mutation :
            self.population.mutation_non_binary(mutation_rate)

            if self.population.population[0].fitness == max :
                same_result = same_result + 1

            if same_result == 5 :
                migration = True
            i = i + 1
            max = self.population.population[0].fitness
            if (i == maxIteration):
                break

        #interface.result.append('the best solution found : \n'+
        #               self.population.population[0].text() )
        return self.population.population[0].fitness, self.population.population[0]








    def run_non_binary(self, maxIteration, mutation_rate):

        #print(self.window.result.toPlainText())
        i = 0
        while True:
            self.population.sort()

            #self.window.addTextDetailedExec('the best solution found till now :\n' +
            #                               self.population.population[0].text())
            self.population.population[0].show()
            # the crossover : monopoint
            self.population.crossover_non_binary()
            # the mutation :
            self.population.mutation_non_binary(mutation_rate)
            i = i + 1
            if (i == maxIteration):
                break

        #interface.result.append('the best solution found : \n'+
        #               self.population.population[0].text() )
        return self.population.population[0].fitness, self.population.population[0]






def runbinary(self, maxIteration, mutation_rate, crossover_point):
    i = 0
    while True:
        self.population.sort()
        #print("the best solution found till now :")
        self.population.population[0].show()
        # the crossover : monopoint
        self.population.crossover(crossover_point)
        # the mutation :
        self.population.mutation(mutation_rate)
        i = i + 1
        if (i == maxIteration):
            break
    #print("the end of the research :\n----------------------")
    #print("the best solution found : ")
    self.population.population[0].show()
    #print("the max fitness of the benchmark ", self.bench.calculmax())
