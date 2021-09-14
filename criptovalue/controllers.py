from criptovalue.models import CriptoValueModel
from criptovalue.views import CriptoValueView, Exchanger

from tkinter import *
from tkinter import ttk

class CriptoValueController():
    def __init__(self):
        self.modelo = CriptoValueModel()
        self.vista = CriptoValueView()

    def ejecuta(self):
        seguir = 's'
        while seguir == 's':
            self.modelo.de, self.modelo.a = self.vista.pedir()
            self.modelo.obtener()
            self.vista.muestra(self.modelo.de, self.modelo.a, self.modelo.valor)

            seguir = input("Quieres más (S/N): ").lower()


class Controller(Tk):
    def __init__(self):
        super().__init__()
        self.title("Consulta valor de criptos")
        self.changer = Exchanger(self, self.probatina)
        self.changer.pack(side=TOP)
        self.modelo = CriptoValueModel()

    def probatina(self):
        print("Calcular cambio entre", self.changer.moneda_desde(), self.changer.moneda_hasta())
        self.modelo.de = self.changer.moneda_desde()
        self.modelo.a = self.changer.moneda_hasta()
        self.modelo.obtener()
        self.changer.set_valor(self.modelo.valor)

