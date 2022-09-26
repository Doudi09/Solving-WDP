# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!
import timeit

import GA
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox

from GA.Benchmark import Benchmark
from GA.GeneticAlgorithm import GeneticAlgorithm


class Ui_Dialog(object):



    def setupUi(self, Dialog):
        # variables :
        self.mutation = 20
        self.iteration = 500
        self.size = 50
        self.length = 1500
        self.path = ''

        Dialog.setObjectName("Dialog")
        Dialog.resize(1278, 820)
        Dialog.setAutoFillBackground(False)
        self.choose_file = QtWidgets.QPushButton(Dialog)
        self.choose_file.setGeometry(QtCore.QRect(440, 190, 161, 51))
        self.choose_file.setObjectName("choose_file")
        # -----------------------------------------------------------
        self.choose_file.clicked.connect(self.select_file)

        self.inter_manually = QtWidgets.QPushButton(Dialog)
        self.inter_manually.setGeometry(QtCore.QRect(1050, 180, 161, 51))
        self.inter_manually.setObjectName("inter_manually")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 280, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.detailed_exe = QtWidgets.QTextBrowser(Dialog)
        self.detailed_exe.setGeometry(QtCore.QRect(20, 400, 511, 391))
        self.detailed_exe.setObjectName("detailed_exe")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 330, 151, 61))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(970, 300, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(960, 370, 131, 16))
        self.label_7.setObjectName("label_7")
        self.population_size = QtWidgets.QTextEdit(Dialog)
        self.population_size.setGeometry(QtCore.QRect(1090, 370, 104, 31))
        self.population_size.setObjectName("population_size")
        # ---------------------------------------------
        self.population_size.setText("50")

        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(960, 440, 131, 16))
        self.label_8.setObjectName("label_8")
        self.object_number = QtWidgets.QTextEdit(Dialog)
        self.object_number.setGeometry(QtCore.QRect(1090, 440, 104, 31))
        self.object_number.setObjectName("object_number")
        # ----------------------------------
        self.object_number.setText("1500")

        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(960, 520, 131, 16))
        self.label_9.setObjectName("label_9")
        self.iteration_number = QtWidgets.QTextEdit(Dialog)
        self.iteration_number.setGeometry(QtCore.QRect(1090, 520, 104, 31))
        self.iteration_number.setObjectName("iteration_number")
        # -------------------
        self.iteration_number.setText("500")

        self.mutation_rate = QtWidgets.QTextEdit(Dialog)
        self.mutation_rate.setGeometry(QtCore.QRect(1090, 600, 104, 31))
        self.mutation_rate.setObjectName("mutation_rate")
        # -------------------
        self.mutation_rate.setText("20")

        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(960, 600, 131, 16))
        self.label_10.setObjectName("label_10")
        self.set_button = QtWidgets.QPushButton(Dialog)
        self.set_button.setGeometry(QtCore.QRect(980, 680, 201, 51))
        self.set_button.setObjectName("set_button")
        # -------------------------
        self.set_button.clicked.connect(self.set_parameters)

        self.run = QtWidgets.QPushButton(Dialog)
        self.run.setGeometry(QtCore.QRect(340, 280, 321, 51))
        self.run.setObjectName("run")
        self.result = QtWidgets.QTextBrowser(Dialog)
        self.result.setGeometry(QtCore.QRect(560, 400, 351, 321))
        self.result.setObjectName("result")
        self.design_graphe = QtWidgets.QPushButton(Dialog)
        self.design_graphe.setGeometry(QtCore.QRect(640, 740, 201, 51))
        self.design_graphe.setObjectName("design_graphe")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 190, 341, 61))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(230, 50, 301, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(220, 0, 561, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setStyleSheet("color : rgb(20, 32, 52);\n"
                                 "")
        self.label.setObjectName("label")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(20, 10, 161, 151))
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("../algo4.jpg"))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")
        self.file_path = QtWidgets.QTextEdit(Dialog)
        self.file_path.setGeometry(QtCore.QRect(620, 190, 311, 41))
        self.file_path.setObjectName("file_path")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.choose_file.setText(_translate("Dialog", "choose a file"))
        self.inter_manually.setText(_translate("Dialog", "Inter manually"))
        self.label_4.setText(_translate("Dialog", "Results :"))
        self.label_5.setText(_translate("Dialog", "Detailed execution"))
        self.label_6.setText(_translate("Dialog", "Parameters settings :"))
        self.label_7.setText(_translate("Dialog", "Population size :"))
        self.label_8.setText(_translate("Dialog", "object number"))
        self.label_9.setText(_translate("Dialog", "Iteration number"))
        self.label_10.setText(_translate("Dialog", "Mutation rate :"))
        self.set_button.setText(_translate("Dialog", "SET"))
        self.run.setText(_translate("Dialog", "RUN"))
        self.run.clicked.connect(self.run_prg)

        self.design_graphe.setText(_translate("Dialog", "Design graph"))
        self.label_3.setText(_translate("Dialog", "Choose the way that you want to\n"
                                                  " add your benchmark"))
        self.label_2.setText(_translate("Dialog", "Using Genetic algorithm"))
        self.label.setText(_translate("Dialog", "WINNER DETERMINATION PROBLEM "))

    def select_file(self):
        name = QFileDialog.getOpenFileName()
        if name[0]:
            print(name[0])
            self.path = name[0]
            self.file_path.setText(name[0])

    def set_parameters(self):
        print('the set function ')
        self.mutation = int(self.mutation_rate.toPlainText())

        self.iteration = int(self.iteration_number.toPlainText())
        self.size = int(self.population_size.toPlainText())
        self.length = int(self.object_number.toPlainText())



    def run_non_binary_ga(self, maxIteration, mutation_rate, ga):
        print('the run method ')
        print(maxIteration)
        print(mutation_rate)

        self.result.append("the result is :")
        self.result.repaint()
        i = 0
        while True:
            print('the loop while ')
            ga.population.sort()
            print("the best solution found till now :")

            #self.result.append('the best solution found till now :\n'+ga.population.population[0].text())
            #self.result.repaint()

            print("the best solution found till now :")

            ga.population.population[0].show()
            # the crossover : monopoint
            ga.population.crossover_non_binary()
            # the mutation :
            ga.population.mutation_non_binary(mutation_rate)
            i = i + 1
            if (i == maxIteration):
                break



        print("the end of the research :\n----------------------")
        self.result.append("the end of the research :\n----------------------")
        self.result.repaint()
        print("the best solution found : \n")
        ga.population.population[0].show()
        print("the max fitness of the benchmark ", self.bench.calculmax())
        # return self.population.population[0].fitness, self.population.population[0]
        #self.result.append("the best solution found : ")
        #self.result.repaint()

    def run_prg(self):

        self.result.append('the result ')
        self.result.append('\n--------')
        self.result.repaint()
        if self.path == '':
            print("error")
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("ERROR !")
            msg.setInformativeText("Would you please enter the file path !!")
            x = msg.exec_()


        else:
            print("else")
            print(self.path)

            bench = Benchmark(self.path)

            start = timeit.default_timer()
            print(start)
            print(self.size)
            print(self.length)
            print(self.iteration)
            print(self.mutation)

            # print(self.result.text())

            ga = GeneticAlgorithm(self.size, self.length, bench, self)

            # best_solution_found_fitness, best_solution_found = ga.run_non_binary(self.iteration, self.mutation, self.result, self.detailed_exe)
            # ga.run_non_binary(self.iteration, self.mutation, self.result, self.detailed_exe)
            # ga.run_non_binary(self.iteration, self.mutation)
            self.run_non_binary_ga(self.iteration, self.mutation, ga)
            end = timeit.default_timer()
            time = end - start
            # self.result.setText('the best solution found :\n'+best_solution_found+'\nfitness value : '+best_solution_found_fitness+
            #                   '\nexecution time : '+time+' sec')


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
