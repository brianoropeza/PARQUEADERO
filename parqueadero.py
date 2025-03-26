import tkinter as tk
from tkinter import font
from datetime import datetime

class SistemaRegistroVehiculos:
    def __init__(self):
        
        self.vehiculos = []

        self.ventana = tk.Tk()
        self.ventana.title("Sistema de Registro de Vehículos")
        self.ventana.geometry("500x500")
        self.ventana.config(bg="#f0f8ff")

        self.fuente_titulo = font.Font(family="Helvetica", size=12, weight="bold")
        self.fuente_texto = font.Font(family="Arial", size=10)
        self.fuente_boton = font.Font(family="Arial", size=10, weight="bold")

        self.label_placa = tk.Label(self.ventana, text="Placa (ABC-123):", font=self.fuente_titulo, bg="#f0f8ff")
        self.entry_placa = tk.Entry(self.ventana, font=self.fuente_texto, bd=2, relief="solid", bg="#e0f7fa")
        self.label_marca = tk.Label(self.ventana, text="Marca:", font=self.fuente_titulo, bg="#f0f8ff")
        self.entry_marca = tk.Entry(self.ventana, font=self.fuente_texto, bd=2, relief="solid", bg="#e0f7fa")
        self.label_color = tk.Label(self.ventana, text="Color:", font=self.fuente_titulo, bg="#f0f8ff")
        self.entry_color = tk.Entry(self.ventana, font=self.fuente_texto, bd=2, relief="solid", bg="#e0f7fa")
        self.label_tipo = tk.Label(self.ventana, text="Tipo (Residente/Visitante):", font=self.fuente_titulo, bg="#f0f8ff")
        self.entry_tipo = tk.Entry(self.ventana, font=self.fuente_texto, bd=2, relief="solid", bg="#e0f7fa")
        
        self.label_mensaje = tk.Label(self.ventana, text="", fg="red", font=self.fuente_texto, bg="#f0f8ff")

        self.boton_guardar = tk.Button(self.ventana, text="Guardar", font=self.fuente_boton, bg="#66bb6a", fg="white", command=lambda: self.guardar_registro())
        self.boton_limpiar = tk.Button(self.ventana, text="Limpiar", font=self.fuente_boton, bg="#ff7043", fg="white", command=lambda: self.limpiar_campos())
        self.boton_mostrar = tk.Button(self.ventana, text="Mostrar Registro", font=self.fuente_boton, bg="#42a5f5", fg="white", command=lambda: self.mostrar_registro())

        self.label_placa.grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.entry_placa.grid(row=0, column=1, padx=10, pady=5)

        self.label_marca.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.entry_marca.grid(row=1, column=1, padx=10, pady=5)

        self.label_color.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.entry_color.grid(row=2, column=1, padx=10, pady=5)

        self.label_tipo.grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.entry_tipo.grid(row=3, column=1, padx=10, pady=5)

        self.label_mensaje.grid(row=4, column=0, columnspan=2, pady=10)

        self.boton_guardar.grid(row=5, column=0, padx=10, pady=10)
        self.boton_limpiar.grid(row=5, column=1, padx=10, pady=10)
        self.boton_mostrar.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

        self.frame_registros = tk.Frame(self.ventana, bg="#f0f8ff")
        self.frame_registros.grid(row=7, column=0, columnspan=2, padx=10, pady=10, sticky="w")

        self.ventana.mainloop()

    def validar_campos(self):
        if (not self.entry_placa.get() or
            not self.entry_marca.get() or
            not self.entry_color.get() or
            not self.entry_tipo.get()):
            self.label_mensaje.config(text="Todos los campos son obligatorios", fg="red")
            return False
        self.label_mensaje.config(text="", fg="red")
        return True

    def guardar_registro(self):
        if self.validar_campos():
            placa = self.entry_placa.get()
            marca = self.entry_marca.get()
            color = self.entry_color.get()
            tipo = self.entry_tipo.get()
            hora_ingreso = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            vehiculo = {
                "placa": placa,
                "marca": marca,
                "color": color,
                "tipo": tipo,
                "hora_ingreso": hora_ingreso
            }

            self.vehiculos.append(vehiculo)

            self.limpiar_campos()
            print(f"Vehículo {placa} registrado exitosamente.")

    def limpiar_campos(self):
        self.entry_placa.delete(0, 'end')
        self.entry_marca.delete(0, 'end')
        self.entry_color.delete(0, 'end')
        self.entry_tipo.delete(0, 'end')

    def mostrar_registro(self):
        for widget in self.frame_registros.winfo_children():
            widget.destroy()

        if not self.vehiculos:
            self.label_mensaje.config(text="No hay registros disponibles.", fg="red")
        else:
            self.label_mensaje.config(text="Registros de vehículos:", fg="black")
            row = 0
            for vehiculo in self.vehiculos:
                print(f"Placa: {vehiculo['placa']}, Marca: {vehiculo['marca']}, Color: {vehiculo['color']}, "
                      f"Tipo: {vehiculo['tipo']}, Hora de Ingreso: {vehiculo['hora_ingreso']}")

                label_info = tk.Label(self.frame_registros, text=f"Placa: {vehiculo['placa']}, Marca: {vehiculo['marca']}, "
                                                                f"Color: {vehiculo['color']}, Tipo: {vehiculo['tipo']}, "
                                                                f"Hora: {vehiculo['hora_ingreso']}",
                                      font=self.fuente_texto, bg="#f0f8ff")
                label_info.grid(row=row, column=0, sticky="w", padx=5, pady=5)
                row += 1

if __name__ == "__main__":
    app = SistemaRegistroVehiculos()

