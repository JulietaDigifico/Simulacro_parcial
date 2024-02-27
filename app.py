import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Julieta
apellido: Digifico
---
Parcial: simulacro
---
Enunciado:
Se desea desarrollar un programa que permita al usuario ingresar el nombre, año emitido (inferior al 2000, Superior a 2000 e inferior a 2015 y superior al 2015), si es online u offline y costo (500 a 10000) de 10 videojuegos.
Realizar las siguientes operaciones:

A - Encontrar el videojuego más caro y el más barato ingresado.
B - Calcular el promedio de los costos de los videojuegos, pero solo para aquellos que son online.
C - Encontrar los videojuegos con el costo máximo y mínimo de aquellos emitidos antes de 2015.
D - Calcular el porcentaje de videojuegos offline en relación al total de videojuegos ingresados.
E - Informar a que rango de año emitido pertenecen la mayor parte de los videojuegos vendidos.

'''
class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        contador_online = 0
        contador_offline = 0
        acumulador_online = 0
        acumulador_offline = 0
        precio_maximo = float('-inf')
        precio_minimo = float('inf')
        cantidad_emision_antes_2015 = 0
        cantidad_emision_despues_2015 = 0
        cantidad_emision_entre_2000_2015 = 0
        precio_maximo_antes_2015 = float('-inf')
        precio_minimo_antes_2015 = float('inf')
        precio_maximo_despues_2015 = float('-inf')
        precio_minimo_despues_2015 = float('inf')
        precio_maximo_entre_2000_2015 = float('-inf')
        precio_minimo_entre_2000_2015 = float('inf')
        CANTIDAD_ITERACIONES = 10

        for i in range(0, CANTIDAD_ITERACIONES):
            print("Videojuego", i + 1)

            nombre = None

            tipo = prompt("Tipo", "Ingrese el tipo de videojuego (online o offline)").upper()

            while True:
                match tipo:
                    case "ONLINE":
                        print("Online")
                        break
                    case "OFFLINE":
                        print("Offline")
                        break
                    case _:
                        print("Error")
                        tipo = prompt ("Error", "Por favor, ingrese correctamente si el videojuego es OFFLINE o ONLINE")

            while nombre == "" or nombre == None:
                nombre = prompt("Nombre", "Ingrese el nombre del videojuego")

            while True:
                emision = prompt("Emision", "Ingrese en que año fue emitido el videojuego")
                if emision == None or int(emision) > 2024:
                    alert("ERROR", "ingresar correctamente el año de emision")
                else:
                    break

            emision = int(emision)

            precio = prompt("Valor", "Ingrese el precio del videojuego")

            precio = int(precio)
            if precio > precio_maximo:
                precio_maximo = precio
            if precio < precio_minimo:
                precio_minimo = precio

            if tipo == "Online":
                acumulador_online += precio

            if emision < 2015:
                 if precio > precio_maximo_antes_2015:
                     precio_maximo_antes_2015 = precio
                 if precio < precio_minimo_antes_2015:
                     precio_minimo_antes_2015 = precio

            if contador_online > 0:
                promedio_precio_online = acumulador_online / contador_online
                print(f"El promedio de precios para videojuegos en línea es: {promedio_precio_online}")

            porcentaje_offline = (contador_offline / CANTIDAD_ITERACIONES) * 100

            if cantidad_emision_antes_2015 > cantidad_emision_despues_2015 and cantidad_emision_antes_2015 > cantidad_emision_entre_2000_2015:
                print("La mayor parte de los videojuegos vendidos fueron emitidos antes de 2015.")
            elif cantidad_emision_despues_2015 > cantidad_emision_entre_2000_2015:
                print("La mayor parte de los videojuegos vendidos fueron emitidos después de 2015.")
            else:
                print("La mayor parte de los videojuegos vendidos fueron emitidos entre 2000 y 2015.")
                     

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()