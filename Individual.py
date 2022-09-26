import random as rn


class Individual:
    """it worked but i got
    stock with the crossover mutation operations ....
    the solution is  vector with max lenght is n (offernumbers) """

    def __init__(self, maxLenght, bench):
        self.maxLenght = maxLenght
        # initialse the solution with zeros
        self.solution = []
        self.fitness = 0.0
        # generating  solution using the K idk what method :
        rand = rn.sample([p / maxLenght for p in range(1, maxLenght + 1)], maxLenght)
        #print("the arndom array ",rand)
        stop = len(rand)
        while stop != 0:
            # getting the max
            maxIndex = rand.index(max(rand))
            # verify if we can add this maxIndex to the solution generated till now:
            # we add 1 to the maxIndex cuz it starts from 0 end in the benchs it does from 1...
            if (bench.verifynonbinary(self.solution, maxIndex)):
                # we add it to the solution
                self.solution.append(maxIndex)
            # deleting the max from th erandom array --> replacing it with -1
            rand[maxIndex] = -1
            stop = stop - 1
        # now that we have the solution we evaluate the fitness function
        self.calculfitnessnonbinary(benchmark=bench)

    """
    
    def __init__(self, maxLenght, bench):
        self.maxLenght = maxLenght
        # initialse the solution with zeros
        self.solution = []
        self.fitness = 0.0
        # generating  solution using the K idk what method :
        rand = rn.sample([p / maxLenght for p in range(1, maxLenght + 1)], maxLenght)
        # print("the arndom array ",rand)
        stop = len(rand)
        while stop != 0:
            # getting the max
            # print("the max is ",max(rand))
            # print("the max index :",rand.index(max(rand)))
            maxIndex = rand.index(max(rand))
            # verify if we can add this maxIndex to the solution generated till now:
            # we add 1 to the maxIndex cuz it starts from 0 end in the benchs it does from 1...
            if (bench.verifynonbinary(self.solution, maxIndex)):
                # we add it to the solution
                self.solution.append(maxIndex)
            # deleting the max from th erandom array --> replacing it with -1
            rand[maxIndex] = -1
            stop = stop - 1
        # now that we have the solution we evaluate the fitness function
        self.calculfitnessnonbinary(benchmark=bench)

    """


    def getGene(self, i):
        return self.solution.__getitem__(i)

    def calculfitnessnonbinary(self, benchmark):
        self.fitness = benchmark.evaluatenonbinary(self)

    def show(self):
        print(self.solution)
        print(self.fitness)

    def __str__(self):
        msq = "["
        for w in self.solution:
            if (msq == "["):
                msq = msq + str(w)
            else:
                msq = msq + ", " + str(w)
        msq = msq + " ]"
        return msq

    def text(self):
        return self.solution + '\n' + self.fitness

    # the mutation is done by tacking the a random offer or the best offer ever
    # adding it to the solution :
    # deleting the commen offer from th solution
    # deleting one offer who have common object with the solution (we delete the offer with the min price)

    """
    
    def mutation(self, mutation_rate, bench):
        rw = rn.random() * 100
        if (rw < mutation_rate):
            new_offer = int(rn.random() * len(self.solution))
        else:
            # picking the best offer
            new_offer = bench.best
        # adding it to the solution :
        # if it doesnt exist otherwise
        if (not new_offer in self.solution):
            for w in self.solution:
                if (bench.bench[w].havecommonobjectwith(bench.bench[new_offer])):
                    if (bench.bench[w].price < bench.bench[new_offer].price):
                        self.solution.remove(w)
                        #self.solution[w] = new_offer
                        self.solution.append(new_offer)
                        break
        #self.solution = set(self.solution)
        #self.solution = list(self.solution)

        self.calculfitnessnonbinary(bench)
        """


    def mutation(self, mutation_rate, bench):
        rw = rn.random() * 100
        if (rw < mutation_rate):
            new_offer = int(rn.random() * len(self.solution))
        else:
            # picking the best offer
            new_offer = bench.best
        # adding it to the solution :
        # if it doesnt exist otherwise
        new_solution = self.solution + [new_offer]

        new_solution = set(new_solution)
        new_solution = list(new_solution)
        for i in range(0, len(new_solution) - 1):
            # while (j < len(new_solution)):
            for j in range(0, len(new_solution)):
                # print(new_solution[i])
                # print("j ", j)
                # print(new_solution[j])
                if (new_solution[j] != -1 and new_solution[i] != -1 and i != j):
                    if (bench.bench[new_solution[i]].havecommonobjectwith(bench.bench[new_solution[j]])):
                        # print("have common object ")
                        if (bench.bench[new_solution[i]].price < bench.bench[new_solution[j]].price):
                            new_solution[i] = -1
                            # new_solution.remove(new_solution[i])

                        else:
                            new_solution[j] = -1
                            # new_solution.remove(new_solution[j])

        # deleting the -1 :
        new_solution = [w for w in new_solution if w != -1]
        self.solution = new_solution

        self.calculfitnessnonbinary(bench)






    # the crossover operation is done by combinig the two solution together
    # deleting the commen offer from th solution
    # deleting one offer who have common object with the solution (we delete the offer with the min price)

    """
    
    def crossover(self, individual, bench):
        new_solution = self.solution + individual.solution
        # deleting the dupliacted offer
        new_solution = set(new_solution)
        new_solution = list(new_solution)
        # print(new_solution)
        # print("len ", len(new_solution))
        # while (i < len(new_solution) - 1):
        for i in range(0, len(new_solution) - 1):
            # while (j < len(new_solution)):
            for j in range(i + 1, len(new_solution)):
                # print(new_solution[i])
                # print("j ", j)
                # print(new_solution[j])
                if (new_solution[j] != -1 and new_solution[i] != -1):
                    if (bench.bench[new_solution[i]].havecommonobjectwith(bench.bench[new_solution[j]])):
                        # print("have common object ")
                        if (bench.bench[new_solution[i]].price < bench.bench[new_solution[j]].price):
                            new_solution[i] = -1
                            # new_solution.remove(new_solution[i])

                        else:
                            new_solution[j] = -1
                            # new_solution.remove(new_solution[j])

        # deleting the -1 :
        new_solution = [w for w in new_solution if w != -1]
        individual = Individual(len(new_solution), bench)
        individual.solution = new_solution
        individual.calculfitnessnonbinary(bench)
        return individual

        """

    def crossover(self, individual, bench):
        new_solution = self.solution + individual.solution
        # deleting the dupliacted offer
        new_solution = set(new_solution)
        new_solution = list(new_solution)
        # print(new_solution)
        # print("len ", len(new_solution))
        # while (i < len(new_solution) - 1):
        for i in range(0, len(new_solution) - 1):
            # while (j < len(new_solution)):
            for j in range(0, len(new_solution)):
                # print(new_solution[i])
                # print("j ", j)
                # print(new_solution[j])
                if (new_solution[j] != -1 and new_solution[i] != -1 and i != j ):
                    if (bench.bench[new_solution[i]].havecommonobjectwith(bench.bench[new_solution[j]])):
                        # print("have common object ")
                        if (bench.bench[new_solution[i]].price < bench.bench[new_solution[j]].price):
                            new_solution[i] = -1
                            # new_solution.remove(new_solution[i])

                        else:
                            new_solution[j] = -1
                            # new_solution.remove(new_solution[j])

        # deleting the -1 :
        new_solution = [w for w in new_solution if w != -1]
        individual = Individual(len(new_solution), bench)
        individual.solution = new_solution
        print("new sol ",new_solution)
        print("indiv sol  ",individual.solution)
        individual.calculfitnessnonbinary(bench)
        return individual


"""

    def trytoreproduce(self, position, bench):
    elemnts = self.solution[:position]
    rand = rn.sample([p / self.maxLenght for p in range(1, self.maxLenght + 1)], self.maxLenght)
    # deleting the elemnts wich they already exist :
    for w in elemnts:
        rand[w] = 0
    stop = len(rand)
    while stop != 0:
        # getting the max
        maxIndex = rand.index(max(rand))
        # verify if we can add this maxIndex to the solution generated till now:
        # we add 1 to the maxIndex cuz it starts from 0 end in the benchs it does from 1...
        if (bench.verify(self.solution, maxIndex) and rand[maxIndex] != 0):
            # we add it to the solution
            self.solution.append(maxIndex)
        # deleting the max from th erandom array --> replacing it with -1
        rand[maxIndex] = -1
        stop = stop - 1
    # now that we have the solution we evaluate the fitness function
    self.calculfitness(benchmark=bench)


"""

"""


#the solution is like the classic GA olution
#a binary one

def __init__(self, maxLenght, bench):
    self.maxLenght = maxLenght
    self.solution = []
    self.fitness = 0.0
    for i in range(0, maxLenght):
        #generating a solution :
        self.solution.append(int(rn.random() * 2))
    self.calculfitness(benchmark=bench)


def getGene(self, i):
    return self.solution.__getitem__(i)

def calculfitness(self, benchmark):
    self.fitness = benchmark.evaluate(self)

def show(self):
    print(self.solution)
    print("the solution fitness : ",self.fitness)



def mutation(self,mutatation_rate,bench):
    #print("the nbr of mutated elements ",int(mutatation_rate*self.maxLenght/100))
    for i in range(0,int(mutatation_rate*self.maxLenght/100)):
        pos = int(rn.random()*self.maxLenght)
        #inversing the bit
        self.solution[pos] = (self.solution[pos]+1)%2

    self.calculfitness(bench)
    #print("the mutation operation")
    #print(self.fitness)


def crossover(self,individual,crossover_point,bench):
    new_elemnt = Individual(self.maxLenght,bench)

    for i in range(0,self.maxLenght):
        if(i>crossover_point):
            new_elemnt.solution[i] = individual.solution[i]
        else:
            new_elemnt.solution[i] = self.solution[i]
    new_elemnt.calculfitness(bench)
    return new_elemnt
    
"""
