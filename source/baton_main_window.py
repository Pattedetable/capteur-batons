#
# Copyright 2021-2023 Manuel Barrette
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#


import serial, io
import serial.tools.list_ports
from PyQt5 import QtGui, QtWidgets
import pyqtgraph as pg
import numpy as np
import matplotlib.pyplot as plt
from pyqtgraph.Qt import QtCore
import platform, os, time
import locale, ctypes

class Ui_MainWindow(object):
    def setupUi(self, MainWindow, parent):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        self.btn = QtWidgets.QPushButton(self.centralwidget)
        self.gridLayout.addWidget(self.btn, 0, 0, 1, 2)

        self.btn2 = QtWidgets.QPushButton(self.centralwidget)
        self.gridLayout.addWidget(self.btn2, 1, 0, 1, 2)

        self.btn3 = QtWidgets.QPushButton(self.centralwidget)
        self.gridLayout.addWidget(self.btn3, 12, 0, 1, 2)

        self.btn4 = QtWidgets.QPushButton(self.centralwidget)
        self.gridLayout.addWidget(self.btn4, 2, 0, 1, 2)

        self.btn5 = QtWidgets.QPushButton(self.centralwidget)
        self.gridLayout.addWidget(self.btn5, 13, 0, 1, 2)

        self.btn6 = QtWidgets.QPushButton(self.centralwidget)
        self.gridLayout.addWidget(self.btn6, 4, 0, 1, 2)

        self.btn7 = QtWidgets.QPushButton(self.centralwidget)
        self.gridLayout.addWidget(self.btn7, 9, 0, 1, 2)

        self.btn8 = QtWidgets.QPushButton(self.centralwidget)
        self.gridLayout.addWidget(self.btn8, 10, 0, 1, 2)

        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setText("M min")
        self.gridLayout.addWidget(self.label1, 5, 0, 1, 1)

        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setText("V min")
        self.gridLayout.addWidget(self.label2, 6, 0, 1, 1)

        self.label3 = QtWidgets.QLabel(self.centralwidget)
        self.label3.setText("M max")
        self.gridLayout.addWidget(self.label3, 7, 0, 1, 1)

        self.label4 = QtWidgets.QLabel(self.centralwidget)
        self.label4.setText("V max")
        self.gridLayout.addWidget(self.label4, 8, 0, 1, 1)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)

        self.text1 = QtWidgets.QLineEdit(self.centralwidget)
        self.text1.setSizePolicy(sizePolicy)
        self.gridLayout.addWidget(self.text1, 5, 1, 1, 1)

        self.text2 = QtWidgets.QLineEdit(self.centralwidget)
        self.text2.setSizePolicy(sizePolicy)
        self.gridLayout.addWidget(self.text2, 6, 1, 1, 1)

        self.text3 = QtWidgets.QLineEdit(self.centralwidget)
        self.text3.setSizePolicy(sizePolicy)
        self.gridLayout.addWidget(self.text3, 7, 1, 1, 1)

        self.text4 = QtWidgets.QLineEdit(self.centralwidget)
        self.text4.setSizePolicy(sizePolicy)
        self.gridLayout.addWidget(self.text4, 8, 1, 1, 1)

        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem, 11, 0, 1, 2)

        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem2, 3, 0, 1, 2)


        self.plot = pg.PlotWidget()
        self.gridLayout.addWidget(self.plot, 0, 2, 14, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        # Initial parameters
        self.retranslateUi(MainWindow)
        self.temps = 0.0

        self.readParams()


###########################################################

# Parameters tests

        # Strain 1 (pour petites charges)
#        self.V_min = 342.0
#        self.M_min = 0.0 # Masse en g
#        self.V_max = 127.0
#        self.M_max = 20988.44 # Masse en g

#        # Strain 1 (pour grosses charges)
#        self.V_min = 336.2
#        self.M_min = 0.0 # Masse en g
#        self.V_max = 320.2
#        self.M_max = 17000.0 # Masse en g

##        # Strain 2
##        self.V_min = 338.0
##        self.M_min = 0.0
##        self.V_max = 124.0
##        self.M_max = 20988.44
#
##        # Strain 1
##        self.V_min = 342.0
##        self.M_min = 0.0
##        self.V_max = 127.0
##        self.M_max = 20988.44

#        # Strain 1 2023 avec ressort
#        self.V_min = 359.0 # 355 a l'envers
#        self.M_min = 0.0
#        self.V_max = 175.0 # 171 a l'envers
#        self.M_max = 17.98675 # en kg

#        # Strain 1 2023 avec ressort
#        self.V_min = 370.0 # 355 a l'envers
#        self.M_min = 0.0
#        self.V_max = 186.0 # 171 a l'envers
#        self.M_max = 17.98675


####################################################


#        # Fit avec grosses charges
#        self.pente = -1.12771979
#        self.ordonnee = 381.68764902

#        # Fit avec petites charges
#        self.pente = -0.09701495
#        self.ordonnee = 45.77428168


####################################################

        self.pente = (self.M_min - self.M_max)/(self.V_min - self.V_max)
        self.ordonnee = - self.pente*self.V_min

        self.baud = 9600                          # baud rate
#        self.filename = 'data.txt'                # log file to save data in
        fps = 10
        self.flagUpdate = False

        self.connexion = True

        self.plot.showGrid(x = True, y = True)
        self.xdata = []
        self.ydata = []

        self.courbe = self.plot.plot(pen=1)

        self.compteur = 0
        self.flagConnexion = 0

        self.connexionold = 0
#        self.outFile = open(self.filename,'w')
        self.timer_recherche = QtCore.QTimer()
        self.timer_recherche.timeout.connect(lambda: self.searchThread(fps))
        self.timer_recherche.start(1000)

        self.timer_lecture = QtCore.QTimer()
        self.timer_lecture.timeout.connect(lambda: self.update(fps))
#        self.timer_lecture.start(int(1000/fps))

        self.displayParams()

        self.disableCalibrate(True)

        # Buttons triggers
        self.btn.clicked.connect(lambda: self.toggleUpdate())
        self.btn2.clicked.connect(lambda: self.effacer())
        self.btn3.clicked.connect(lambda: self.graphique())
        self.btn4.clicked.connect(lambda: self.enregistrer())
        self.btn5.clicked.connect(lambda: self.fermerEtAfficher())
        self.btn7.clicked.connect(lambda: self.updateParams())
        self.btn6.clicked.connect(lambda: self.checkDisabled())
        self.btn8.clicked.connect(lambda: self.displayParams())


    def retranslateUi(self, MainWindow):
        self._translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(self._translate("MainWindow", "Capteur"))
        self.btn.setText(self._translate("MainWindow", "Mettre à jour"))
        self.btn2.setText(self._translate("MainWindow", "Effacer"))
        self.btn4.setText(self._translate("MainWindow", "Enregistrer"))
        nom_bouton = self._translate("MainWindow", "Graphique à partir") + " \n " + self._translate("MainWindow", "d'un fichier")
        self.btn3.setText(nom_bouton)
        self.btn5.setText(self._translate("MainWindow", "Quitter"))
        self.btn6.setText(self._translate("MainWindow", "Calibrer"))
        self.btn7.setText(self._translate("MainWindow", "Accepter"))
        self.btn8.setText(self._translate("MainWindow", "Annuler"))
        self.plot.setLabel('left', text=self._translate("MainWindow", "Force"), units='N')
        #self.plot.setLabel('bottom', text=self._translate("MainWindow", "Position"), units='m')


    def checkDisabled(self):
        if self.btn7.isEnabled():
            self.disableCalibrate(True)
            self.pente = (self.M_min - self.M_max)/(self.V_min - self.V_max)
            self.ordonnee = - self.pente*self.V_min
            self.plot.setLabel('left', text=self._translate("MainWindow", "Force"), units='N')
        else:
            self.disableCalibrate(False)
            self.pente = 1.0/9.81
            self.ordonnee = 0.0
            self.plot.setLabel('left', text=self._translate("MainWindow", "Voltage"))


    def disableCalibrate(self, choix):
        self.text1.setDisabled(choix)
        self.text2.setDisabled(choix)
        self.text3.setDisabled(choix)
        self.text4.setDisabled(choix)
        self.btn7.setDisabled(choix)
        self.btn8.setDisabled(choix)


    def readParams(self):
        fichier = open("params.dat", "r")
        lines = fichier.readlines()
        contenu = []
        for line in lines:
            contenu.append(line.split(" "))
#        print(contenu)
        self.M_min = float(contenu[0][1])
        self.V_min = float(contenu[1][1])
        self.M_max = float(contenu[2][1])
        self.V_max = float(contenu[3][1])
        fichier.close()
#        print(self.M_min, self.V_min, self.M_max, self.V_max)

    def displayParams(self):
        self.text1.setText(str(self.M_min))
        self.text2.setText(str(self.V_min))
        self.text3.setText(str(self.M_max))
        self.text4.setText(str(self.V_max))


    def updateParams(self):
        self.M_min = float(self.text1.text())
        self.V_min = float(self.text2.text())
        self.M_max = float(self.text3.text())
        self.V_max = float(self.text4.text())
        self.writeParams()
        self.pente = (self.M_min - self.M_max)/(self.V_min - self.V_max)
        self.ordonnee = - self.pente*self.V_min
        self.disableCalibrate(True)


    def writeParams(self):
        fichier = open("params.dat", "w")
        fichier.write("Mmin {}\n".format(self.M_min))
        fichier.write("Vmin {}\n".format(self.V_min))
        fichier.write("Mmax {}\n".format(self.M_max))
        fichier.write("Vmax {}\n".format(self.V_max))
        fichier.close()


    def fermerEtAfficher(self):
        app = QtWidgets.QApplication.instance()
        app.closeAllWindows()


    def toggleUpdate(self):
        self.flagUpdate = not self.flagUpdate
        if self.flagUpdate:
            self.btn.setText(self._translate("MainWindow", "Arrêter"))
            if self.device:
                self.serialPort.reset_input_buffer()
                line = self.serialPort.readline() # Jeter la premiere ligne car souvent incomplete
        else:
            self.btn.setText(self._translate("MainWindow", "Mettre à jour"))
        return None


    def effacer(self):
        self.xdata = []
        self.ydata = []
        self.courbe.setData(self.xdata, self.ydata)
#        self.outFile.seek(0)
#        self.outFile.truncate()
        self.compteur = 0
        self.temps = 0.0
        return None


    def enregistrer(self):
        extension = self._translate("MainWindow", "Données") + " (*.txt)"
        fichier = QtWidgets.QFileDialog.getSaveFileName(None, self._translate("MainWindow", "Enregistrer sous..."), '', extension)
        nom_fichier = fichier[0]
        if nom_fichier != "" and nom_fichier[-4:] != ".txt":
            nom_fichier = nom_fichier + ".txt"
        fichier = open(nom_fichier, 'w')
        for i in range(0,self.compteur):
            sortie = str(self.xdata[i]) + " " + str(self.ydata[i]) + "\n"
            fichier.write(sortie)
        fichier.close()


#    def enregistrer(self):
#        extension = self._translate("MainWindow", "Données") + " (*.txt)"
#        fichier = QtWidgets.QFileDialog.getSaveFileName(None, self._translate("MainWindow", "Enregistrer sous..."), '', extension)
#        nom_fichier = fichier[0]
#        if nom_fichier != "" and nom_fichier[-4:] != ".txt":
#            nom_fichier = nom_fichier + ".txt"
#        systeme_exploitation = platform.system()
#        if systeme_exploitation == 'Windows':
#            commande = 'copy ' + self.filename + ' "' + nom_fichier + '"'
#        else:
#            commande = 'cp ' + self.filename + ' "' + nom_fichier + '"'
#        print(commande)
#        os.system(commande)


    def graphique(self):

        extension = self._translate("MainWindow", "Données") + " (*.txt)"
        fichier = QtWidgets.QFileDialog.getOpenFileName(None, self._translate("MainWindow", "Ouvrir..."), "", extension)

        try:
            lecture = open(fichier[0])
            xdata = []
            ydata = []
            for line in lecture:
                x, y = line.split(" ", 1)
                x = float(x)
                y = float(y)
                xdata.append(x)
                ydata.append(y)
            #plt.xlabel(self._translate("MainWindow", "Position") + " (m)")
            plt.ylabel(self._translate("MainWindow", "Force (N)"))
            plt.plot(xdata, ydata)
            plt.show()
        except(FileNotFoundError):
            pass


    def findDevice(self):
        ports = list(serial.tools.list_ports.comports())
        systeme_exploitation = platform.system()
        for p in ports:
            if systeme_exploitation == 'Windows':
                if "Arduino" in p.description or "USB Serial Device" in p.description or "Périphérique série USB" in p.description:
                    print(p.device)
                    return p.device
            elif systeme_exploitation == 'Linux' and "Arduino" in p.manufacturer:
                print(p.device)
                return p.device
            elif systeme_exploitation == 'Darwin' and "Arduino" in str(p.manufacturer):
                print(p.device)
                return p.device

    def searchThread(self, fps):
        self.device = self.findDevice()
        if self.device:
            print("Connecte")
            time.sleep(1)
            self.serialPort = serial.Serial(self.device,self.baud)
            self.timer_recherche.stop()
            self.timer_lecture.start(int(1000/fps))

    def update(self, fps):
        try:
            line = self.serialPort.readline()
            if self.flagUpdate == True:
                self.compteur = self.compteur + 1
#                line = self.serialPort.readline()
                line2 = line.rstrip()
                y = line2.decode("utf-8")
                x = float(self.temps)
                y = float(y)
                y = float(y)*self.pente + self.ordonnee
                y = 9.81*y#/1000.0
                self.xdata.append(x)
                self.ydata.append(y)
    ##            donnees = str(x) + " " + str(y) + "\n"
    ##            self.outFile.write(donnees)
                self.courbe.setData(self.xdata, self.ydata)
                self.temps = self.temps + 1.0
        except serial.serialutil.SerialException:
            print("Deconnecte")
            self.timer_lecture.stop()
            self.timer_recherche.start(1000)
            self.device = False

