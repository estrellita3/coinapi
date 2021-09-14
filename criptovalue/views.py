  
from tkinter import *
from tkinter import ttk
from criptovalue import MONEDAS

class CriptoValueView():
    def pedir(self):
        de = input("Moneda de origen: ")
        a = input("Moneda de destino: ")

        return de, a

    def muestra(self, origen, destino, valor):
        print(f"1 {origen} vale {valor} {destino}")

def funcion_del_boton():
    print("Click")

class Exchanger(ttk.Frame):
    def __init__(self, parent, funcion_click_del_controlador):
        super().__init__(parent, height=300, width=430)

        self.grid_propagate(0)

        self.desde_valor = StringVar()
        self.desde = ttk.Combobox(self, values=MONEDAS, textvariable = self.desde_valor)
        self.desde.grid(column=0, row=0)

        self.hasta_valor = StringVar()
        self.hasta = ttk.Combobox(self, values=MONEDAS, textvariable = self.hasta_valor)
        self.hasta.grid(column=1, row=0)

        self.valor = ttk.Label(self, anchor=CENTER, text="0.0")
        self.valor.grid(column=0, row=1, columnspan=2)

        self.calcular = ttk.Button(self, text="Calcular", command=funcion_click_del_controlador)
        self.calcular.grid(column=1, row=2)

    def moneda_desde(self):
        return self.desde_valor.get()[:3]

    def moneda_hasta(self):
        return self.hasta_valor.get()[:3]

    def set_valor(self, texto):
        self.valor.config(text=texto)