from builtins import int, set

from GA.Offer import Offer


class Benchmark:
    """list of offers
    """

    def __init__(self, path):
        self.path = path
        self.bench = []
        file = open(path)
        i = 0
        for line in file:
            if (i == 0):
                # this is the firs line :
                self.m = int(line.split()[0])
                self.n = int(line.split()[1])
            else:
                self.bench.append(Offer(line))
            i = i + 1
        self.best = self.bench.index(max(self.bench,key=lambda x : x.price))

    def show(self):
        i = 0
        for w in self.bench:
            print("offre nbr ",i)
            i=i+1
            print(w.show())

    # verify if the solution is accepted
    # if not fit = 0
    # otherwise its the sum of prices :
    def evaluate(self, individual):
        fit = 0.0
        temp = []
        for i in range(0, len(individual.solution)):
            # print("a part of th solution ",i , "  " ,individual.solution[:i])
            if (not self.verifyplease(temp, i) and individual.solution[i]==1):
                return 0
            else:
                if(individual.solution[i]!=0):
                    fit = fit + self.bench.__getitem__(i).price
                    temp.append(i)
        return fit

    def verifysolution(self, individual_solution, offer):
        if (len(individual_solution)==0):
            return True
        for i in range(0, len(individual_solution)):
            if (individual_solution[i] == 1):
                if (self.bench.__getitem__(i).havecommonobjectwith(self.bench.__getitem__(offer))):
                    return False
        return True


    def evaluatenonbinary(self,individual):
        fit = 0.0
        for w in individual.solution:
            fit = fit + self.bench[w].price
        return fit




    def verifyplease(self,solution, offer):
        for s in solution:
            # print("the solution item ",s)
            if (self.bench.__getitem__(s).havecommonobjectwith(self.bench.__getitem__(offer))):
                return False
        return True



    def verifynonbinary(self,solution,maxIndex):
        # verify if the solutions offers and the maxIndex offer have common objects:
        for s in solution:

            if (self.bench[s].havecommonobjectwith(self.bench[maxIndex])):
                return False
        return True


    def verify(self, solution, maxIndex):
        # verify if the solutions offers and the maxIndex offer have common objects:
        for s in solution:
            # print("the solution item ",s)
            if (self.bench.__getitem__(s).havecommonobjectwith(self.bench.__getitem__(maxIndex))):
                return False
        return True

    def calculmax(self):
        max = 0
        for w in self.bench:
            max = max + w.price
        # print("the max is ", max)
        return max
