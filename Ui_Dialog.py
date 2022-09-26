# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!
import timeit
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QApplication

from GA.Benchmark import Benchmark
from GA.GeneticAlgorithm import GeneticAlgorithm



class Ui_Dialog(object):

    def setupUi(self, Dialog):
        # variables :
        self.mutation = 48
        self.iteration = 745
        self.size = 60
        self.tries = 3
        self.path = ''

        self.x = []
        self.y = []

        Dialog.setObjectName("Dialog")
        Dialog.resize(1278, 820)
        Dialog.setAutoFillBackground(False)
        self.choose_file = QtWidgets.QPushButton(Dialog)
        self.choose_file.setGeometry(QtCore.QRect(340, 190, 161, 51))
        # -----------------------------------------------------------
        self.choose_file.clicked.connect(self.select_file)

        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.choose_file.setFont(font)
        self.choose_file.setStyleSheet("border-width: 2px;\n"
                                       "border-radius: 15px;\n"
                                       "background-color: rgb(76, 116, 185);\n"
                                       "color:rgb(255, 255, 255)")
        self.choose_file.setObjectName("choose_file")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(310, 290, 251, 61))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgb(20, 32, 52)")
        self.label_4.setObjectName("label_4")
        self.detailed_exe = QtWidgets.QTextBrowser(Dialog)
        self.detailed_exe.setGeometry(QtCore.QRect(20, 440, 511, 361))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.detailed_exe.setFont(font)
        self.detailed_exe.setObjectName("detailed_exe")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(30, 380, 301, 61))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:#DE781F")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(1010, 320, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color:#DE781F")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(990, 390, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color:rgb(76, 116, 185)")
        self.label_7.setObjectName("label_7")
        self.population_size = QtWidgets.QTextEdit(Dialog)
        self.population_size.setGeometry(QtCore.QRect(1140, 390, 104, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.population_size.setFont(font)
        self.population_size.setStyleSheet("border-width: 2px;\n"
                                           "border-radius: 15px;\n"
                                           "color:rgb(20, 32, 52)")
        self.population_size.setObjectName("population_size")
        # --------------------------------------------------------------------------------
        self.population_size.setText("60")

        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(990, 460, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color:rgb(76, 116, 185)")
        self.label_8.setObjectName("label_8")
        self.number_tries = QtWidgets.QTextEdit(Dialog)
        self.number_tries.setGeometry(QtCore.QRect(1140, 460, 104, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.number_tries.setFont(font)
        self.number_tries.setStyleSheet("border-width: 2px;\n"
                                         "border-radius: 15px;\n"
                                         "color:rgb(20, 32, 52)")
        self.number_tries.setObjectName("object_number")
        # ----------------------------------
        self.number_tries.setText("3")

        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(990, 540, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color:rgb(76, 116, 185)")
        self.label_9.setObjectName("label_9")
        self.iteration_number = QtWidgets.QTextEdit(Dialog)
        self.iteration_number.setGeometry(QtCore.QRect(1140, 540, 104, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.iteration_number.setFont(font)
        self.iteration_number.setStyleSheet("border-width: 2px;\n"
                                            "border-radius: 15px;\n"
                                            "color:rgb(20, 32, 52)")
        self.iteration_number.setObjectName("iteration_number")
        # -------------------
        self.iteration_number.setText("745")

        self.mutation_rate = QtWidgets.QTextEdit(Dialog)
        self.mutation_rate.setGeometry(QtCore.QRect(1140, 620, 104, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.mutation_rate.setFont(font)
        self.mutation_rate.setStyleSheet("border-width: 2px;\n"
                                         "border-radius: 15px;\n"
                                         "color:rgb(20, 32, 52)")
        self.mutation_rate.setObjectName("mutation_rate")
        # -------------------
        self.mutation_rate.setText("48")

        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(990, 620, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color:rgb(76, 116, 185)")
        self.label_10.setObjectName("label_10")
        self.set = QtWidgets.QPushButton(Dialog)
        self.set.setGeometry(QtCore.QRect(1030, 670, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.set.setFont(font)
        self.set.setStyleSheet("border-width: 2px;\n"
                               "border-radius: 15px;\n"
                               "background-color:rgb(0, 177, 112);\n"
                               "color:rgb(255, 255, 255)")
        self.set.setObjectName("set")
        # -------------------------
        self.set.clicked.connect(self.set_parameters)

        self.run = QtWidgets.QPushButton(Dialog)
        self.run.setGeometry(QtCore.QRect(1010, 190, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.run.setFont(font)
        self.run.setStyleSheet("border-width: 2px;\n"
                               "border-radius: 15px;\n"
                               "background-color: rgb(76, 116, 185);\n"
                               "color:rgb(255, 255, 255)")
        self.run.setObjectName("run")
        # ------------------------------------------------------------------------------
        self.run.clicked.connect(self.run_prg)

        self.result = QtWidgets.QTextBrowser(Dialog)
        self.result.setGeometry(QtCore.QRect(580, 450, 351, 241))
        self.result.setObjectName("result")
        font = QtGui.QFont()
        font.setPointSize(14)
        self.result.setFont(font)
        font.setFamily("Calibri")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)

        self.design_graphe = QtWidgets.QPushButton(Dialog)
        self.design_graphe.setGeometry(QtCore.QRect(610, 710, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.design_graphe.setFont(font)
        self.design_graphe.setStyleSheet("border-width: 2px;\n"
                                         "border-radius: 15px;\n"
                                         "background-color:rgb(222, 120, 31);\n"
                                         "color:rgb(255, 255, 255)")
        self.design_graphe.setObjectName("design_graphe")
        # -------------------------------------------------------------
        # add the seign function
        self.design_graphe.clicked.connect(self.designe)

        self.design_graphe.setEnabled(False)
        self.design_graphe.setVisible(False)



        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 190, 301, 61))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:rgb(76, 116, 185)")
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(230, 50, 301, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color : rgb(222, 120, 31)")
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(220, 0, 561, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color : rgb(222, 120, 31)")
        self.label.setObjectName("label")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(20, 10, 171, 151))
        self.label_11.setText("")
        #self.label_11.setPixmap(QtGui.QPixmap("../GUI/img.png"))
        self.label_11.setPixmap(QtGui.QPixmap("img.png"))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")
        self.file_path = QtWidgets.QTextEdit(Dialog)
        self.file_path.setGeometry(QtCore.QRect(530, 190, 451, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.file_path.setFont(font)
        self.file_path.setStyleSheet("border-width: 2px;\n"
                                     "border-radius: 15px;\n"
                                     "color: #142034;\n"
                                     "border-color:rgb(76, 116, 185);")
        self.file_path.setObjectName("file_path")

        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(40, 260, 1221, 20))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.line.setFont(font)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(590, 390, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color:rgb(222, 120, 31)")
        self.label_12.setObjectName("label_12")
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(960, 280, 20, 491))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.set_2 = QtWidgets.QPushButton(Dialog)
        self.set_2.setGeometry(QtCore.QRect(1030, 740, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.set_2.setFont(font)
        self.set_2.setStyleSheet("border-width: 2px;\n"
                                 "border-radius: 15px;\n"
                                 "color:rgb(255, 255, 255);\n"
                                 "background-color:rgb(244, 79, 92)")
        self.set_2.setObjectName("set_2")
        # --------------------------------
        # reset button

        self.set_2.clicked.connect(self.reset)

        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(150, 280, 101, 91))
        self.label_13.setText("")
        #self.label_13.setPixmap(QtGui.QPixmap("../GUI/img2.png"))
        self.label_13.setPixmap(QtGui.QPixmap("img2.png"))
        self.label_13.setScaledContents(True)
        self.label_13.setObjectName("label_13")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "WINNER DETERMINATION PROBLEM"))
        self.choose_file.setText(_translate("Dialog", "choose a file"))
        self.label_4.setText(_translate("Dialog", "Results :"))
        self.label_5.setText(_translate("Dialog", "Detailed execution trace :"))
        self.label_6.setText(_translate("Dialog", "Parameters settings :"))
        self.label_7.setText(_translate("Dialog", "Population size :"))

        self.label_8.setText(_translate("Dialog", "Number of tries"))

        self.label_9.setText(_translate("Dialog", "Iteration number"))

        self.label_10.setText(_translate("Dialog", "Mutation rate :"))

        self.set.setText(_translate("Dialog", "Set"))
        self.run.setText(_translate("Dialog", "RUN"))
        self.design_graphe.setText(_translate("Dialog", "Design graph"))
        self.label_3.setText(_translate("Dialog", "Choose the way that you want to\n"
                                                  " add your benchmark"))
        self.label_2.setText(_translate("Dialog", "Using Genetic algorithm"))
        self.label.setText(_translate("Dialog", "WINNER DETERMINATION PROBLEM "))
        self.label_12.setText(_translate("Dialog", "Final result"))
        self.set_2.setText(_translate("Dialog", "Reset"))

    # -------------------------------------------

    def select_file(self):
        name = QFileDialog.getOpenFileName()
        if name[0]:
            #print(name[0])
            self.path = name[0]
            self.file_path.setText(name[0])

    def set_parameters(self):

        #print('the set function ')
        self.mutation = int(self.mutation_rate.toPlainText())

        self.iteration = int(self.iteration_number.toPlainText())
        self.size = int(self.population_size.toPlainText())
        self.tries = int(self.number_tries.toPlainText())

    def run_prg(self):
        #self.result.append('the result ')
        #self.result.append('\n--------')
        #self.result.repaint()
        if self.path == '':
            print("error")
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("ERROR !")
            msg.setInformativeText("Would you please enter the file path !!")
            msg.exec_()
        else:
            self.detailed_exe.setText("")
            self.result.setText("")
            self.y = []

            bench = Benchmark(self.path)


            for i in range(1,self.tries+1):
                ga = GeneticAlgorithm(self.size, 1500, bench)
                self.detailed_exe.append("<font color='#DE781F'>Creating the benchmark instant ...\n</font>")

                self.detailed_exe.append("<font color='#DE781F'>Creating the Genetic algorithm instant ...\n</font>")
                start = timeit.default_timer()
                self.detailed_exe.append("<font color='#DE781F'>Try number "+str(i)+" :\n\n+\n\n</font>")
                self.result.append("<font color='#DE781F'>Try number "+str(i)+" :\n\n\n\n</font>")
                self.run_non_binary_ga(self.iteration, self.mutation, ga)
                end = timeit.default_timer()
                time = end - start


                m = "<font color='#DE781F'>The execution time : " + str(time) + " second\n\n</font>"
                self.result.append(m)
            self.design_graphe.setVisible(True)
            self.design_graphe.setEnabled(True)

    def reset(self):
        self.mutation = 48
        self.mutation_rate.setText("48")

        self.iteration = 745
        self.iteration_number.setText("745")
        self.size = 60
        self.population_size.setText("60")
        self.tries = 3
        self.number_tries.setText("3")

    # ---------------------------------------------------------

    def run_non_binary_ga(self, maxIteration, mutation_rate, ga):
        #print('the run method ')
        #print(maxIteration)
        #print(mutation_rate)

        #self.result.append("the result is :")
        #self.result.repaint()
        i = 0
        same_result = 0
        migration = False
        best = 0
        #self.y = []

        self.detailed_exe.append("<font color='#4C74B9'>Starting the search ....</font>")
        while True:
            #print('the loop while ')
            ga.population.sort()
            #print("the best solution found till now :")
            m = "<font color='#DE781F'>\nThe best solution found till now :\n</font>" + str(ga.population.population[0])
            self.detailed_exe.append(m)
            self.detailed_exe.append("<font color='#DE781F'>The fitness value :</font>")
            self.detailed_exe.append(str(ga.population.population[0].fitness))
            #.append(ga.population.population[0].fitness)
            self.detailed_exe.repaint()
            ga.population.population[0].show()
            # the crossover : monopoint
            if best == ga.population.population[0].fitness:
                same_result = same_result+1
            if same_result == 5:
                migration = True

            ga.population.crossover_non_binary()
            i = i + 1
            """
            
            if not migration:
                ga.population.crossover_non_binary()
            else:
                ga.population.crossover_non_binary_migration()
            
            """
            # the mutation :
            ga.population.mutation_non_binary(mutation_rate)

            if (i == maxIteration):

                break

        #print("the end of the research :\n----------------------")
        self.detailed_exe.append("<font color='#F44F5C'>The end of search .....</font>")
        self.result.append("<font color='#00B170'>The best solution found :</font>")

        self.result.append("  " + str(ga.population.population[0]))
        self.result.append("<font color='#00B170'>The fitness value :</font>")
        self.result.append(str(ga.population.population[0].fitness))

        #print("the best solution found : \n")
        ga.population.population[0].show()
        self.y.append(ga.population.population[0].fitness)
        #print("the max fitness of the benchmark ", ga.bench.calculmax())


    # ---------------------------------------------------------

    def designe(self):

        print("the graph designe")
        self.x = range(1,self.tries+1)

        from Try.GraphPopUp import GraphPopUp
        self.graph_pop = GraphPopUp(self.x,self.y)
        self.graph_pop.show()


# ----------------------------------------------------------------

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
