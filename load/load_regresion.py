from PyQt5 import QtWidgets, uic
from Regresion_lineal.Caso_de_prueba_1 import RegresionLineal

class VentanaRegresion(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/ventana_regresion_lineal.ui", self)
        self.show()

        self.pushButton.clicked.connect(self.botonPrueba1Click)
        self.pushButton_3.clicked.connect(self.botonPrueba2Click)
        self.pushButton_2.clicked.connect(self.botonPrueba3Click)
        self.pushButton_4.clicked.connect(self.botonPrueba4Click)

    def mostrarResultados(self, caso):
        caso.Calcular()
        self.label_B0.setText(str(caso.B0))
        self.label_B1.setText(str(caso.B1))
        self.label_xry.setText(str(caso.rxy))
        self.label_r2.setText(str(caso.r2))
        self.label_Yk.setText(str(caso.Yk))

    def botonPrueba1Click(self):
        caso1 = RegresionLineal(
            [130,650,99,150,128,302,95,945,368,961],
            [186,699,132,272,291,331,199,1890,788,1601])
        self.mostrarResultados(caso1)

    def botonPrueba2Click(self):
        caso2 = RegresionLineal(
            [130,650,99,150,128,302,95,945,368,961],
            [15,69.9,6.5,22.4,28.4,65.9,19.4,198.7,38.8,138.2])
        self.mostrarResultados(caso2)

    def botonPrueba3Click(self):
        caso3 = RegresionLineal(
            [163,765,141,166,137,355,136,1206,433,1130],)
        self.mostrarResultados(caso3)

    def botonPrueba4Click(self):
        caso4 = RegresionLineal(
            [163,765,141,166,137,355,136,1206,433,1130],
            [15,69.9,6.5,22.4,28.4,65.9,19.4,198.7,38.8,138.2])
        self.mostrarResultados(caso4)