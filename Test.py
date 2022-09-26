from GA.Benchmark import Benchmark
from GA.GeneticAlgorithm import GeneticAlgorithm

import  timeit
from GA.Population import Population

"""
bench = Benchmark("test_file.txt")
population = Population(6,5,bench)
population.sort()
print("the sorted pop ----------------------------------")
population.show()
print("the crossover----------------------------------")
population.crossover_non_binary()
population.show()
print("the mutated pop----------------------------------")
population.mutation_non_binary(10)
population.show()


"""

"""

from PyQt5 import QtWidgets

application = QtWidgets.QApplication([])
w = QtWidgets.QWidget()

w.show()

import timeit

result_file = open("result.txt", "w")
result_file.write("file, time, result")

# for w in range(601, 701):
"""

"""

path = "D:/MES ETUDES/S2/E commerce/PROJET/groupe5/instance/in601"

bench = Benchmark(path)
Ga = GeneticAlgorithm(1, 1500, bench)
print(bench.show())

sol = [388, 825, 1408, 601, 690, 832, 229, 1038, 540, 476]
for s in sol :
    for i in range(len(sol)):
        if s != sol[i] and bench.bench[s].havecommonobjectwith(bench.bench[sol[i]]):
            print("have comm object ")
        else:
            print('offer ',s," and offer ",sol[i]," dont have obj comm")
print ("done ")
"""


"""

Ga.population.show()
sol = Ga.population.population[0]
for s in sol.solution :
    print("s : ",s)
    print(bench.bench[s].show())
#print(Ga.population.show())
"""

"""

results = []
time = []
for w in range(601,611):
    path = "D:/MES ETUDES/S2/E commerce/PROJET/groupe5/instance/in"+str(w)

    bench = Benchmark(path)
    Ga = GeneticAlgorithm(53, 1500, bench)
    start = timeit.default_timer()
    fit, best_solution_found = Ga.run_non_binary(670,32)
    end = timeit.default_timer()
    t =  end - start

    results.append(fit)
    time.append(t)


print(results)
print(time)

"""




# path = "D:/MES ETUDES/S2/E commerce/PROJET/groupe5/instance/in"+str(w)
path = "D:/MES ETUDES/S2/E commerce/PROJET/groupe5/instance/in601"
bench = Benchmark(path)

sol = [709, 550, 247, 71, 1411, 1341, 289, 986, 178, 841, 1205 ]




"""

best_mut = 20
best_pop = 74
best_iter = 791

best = 0


for mut in range(10,100,2):
    Ga = GeneticAlgorithm(best_pop, 1500, bench)
    fit, best_solution_found= Ga.run_non_binary(best_iter, mut)

    if best < fit:
        best = fit
        best_mut = mut


print("the best mut ",best_mut)
print("the best fit ",best)

"""

"""



best = 0
for iteration in range(10,1000,5):
    Ga = GeneticAlgorithm(best_pop, 1500, bench)
    fit, best_solution_found= Ga.run_non_binary(iteration, 20)

    if best < fit:
        best = fit
        best_iter = iteration


print("best iter , ",best_iter)
"""

"""

best = 0
for mutation in range(2,100,1):
    Ga = GeneticAlgorithm(best_pop, 1500, bench)
    fit, best_solution_found= Ga.run_non_binary(best_iter, mutation)

    if best < fit:
        best = fit
        best_mut = mutation


print('the best mutation ',best_mut)


print('the best population ',best_pop)
"""



# reglage de paramètres



"""
best_pop = 10
best_mutation = 1
best_iter = 50
best_fit = 0
# sur les 100 fichiers :
file_path = "D:/MES ETUDES/S2/E commerce/PROJET/groupe5/instance/in"

# reglage de population size :
for w in range(602, 603):
    print('file ', w)
    for pop in range(10, 50, 10):
        bench = Benchmark(file_path + str(w))
        Ga = GeneticAlgorithm(50, pop, bench)
        for mut in range(1,100,2):
            for iter in range(100,1000,100):
                fit, best_solution_found = Ga.run_non_binary(iter, mut)
                print('fit : ',fit)
                if best_fit < fit:
                    best_pop = pop
                    best_fit = fit
                    best_iter = iter
                    best_mutation = mut

    print('\n\nfile ',w)
    print('best pop ',best_pop)
    print('best mutation ',best_mutation)
    print('best iter ',best_iter)
    print('best fit ',best_fit)

"""


"""
result_file.write("\n")
result_file.write(path[52:])
result_file.write(", ")
result_file.write(str(time))
result_file.write(", ")
result_file.write(str(best_solution_found))




result_file.close()
"""
print("------------------------------------------------: ")
# print(idiv.fitness)


"""
200 1 3 5
450 3 2
600 1
"""

"""wher i do my test """
"""

print("hello world")

path = "D:/MES ETUDES/S2/E commerce/PROJET/groupe5/instance/in601"

bench = Benchmark(path)

bench.show()

bench.calculmax()

population = Population(1500,15,bench)
population.show()





path = "D:/MES ETUDES/S2/E commerce/PROJET/groupe5/instance/in601"


bench = Benchmark(path)

Ga = GeneticAlgorithm(50,1500,bench)
Ga.run(100,10,750)






"""
# idiv = Individual(1500,bench)

# idiv.show()


"""


population = Population(6,5,bench)
population.sort()
print("the sorted pop ----------------------------------")
population.show()
print("the crossover----------------------------------")
population.crossover(3)
population.show()
print("the mutated pop----------------------------------")
#population.mutation(10)
population.show()



"""

"""


path = "test_file.txt"

bench = Benchmark(path)

bench.show()

bench.calculmax()
idiv = Individual(6,bench)
idiv.show()

print("the fitness : ")
print(idiv.fitness)

"""
