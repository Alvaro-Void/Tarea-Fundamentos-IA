import customtkinter as ctk
from tkinter import messagebox

# para mostrar matplotlib en tkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# importar función de gráfica
import grafica as gr

# configuración visual
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

# clase principal
class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Funciones lineales")
        self.geometry("900x600")

        self.current_frame = None
        self.cambiar_frame(Menu)

    # cambiar de pantalla
    def cambiar_frame(self, frame_class, *args):
        if self.current_frame is not None:
            self.current_frame.destroy()

        self.current_frame = frame_class(self, *args)
        self.current_frame.pack(fill="both", expand=True)


# pantalla principal
class Menu(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # título
        ctk.CTkLabel(self, text="Generador f(x)=mx+b", font=("Arial", 20)).pack(pady=20)

        # entrada de pendiente
        self.entry_m = ctk.CTkEntry(self, placeholder_text="Pendiente (m)")
        self.entry_m.pack(pady=10)

        # entrada de término independiente
        self.entry_b = ctk.CTkEntry(self, placeholder_text="Término independiente (b)")
        self.entry_b.pack(pady=10)

        # botón para graficar
        ctk.CTkButton(self, text="Graficar", command=self.validar).pack(pady=15)

    # validar datos
    def validar(self):
        m = self.entry_m.get()
        b = self.entry_b.get()

        # verificar vacíos
        if m == "" or b == "":
            messagebox.showerror("Error", "Ingrese valores")
            return

        # verificar que sean números
        try:
            m = float(m)
            b = float(b)
        except:
            messagebox.showerror("Error", "Ingrese números válidos")
            return

        # evitar caso trivial
        if m == 0 and b == 0:
            messagebox.showerror("Error", "Valores no válidos")
            return

        # cambiar a pantalla de gráfica
        self.master.cambiar_frame(GraficaFrame, m, b)


# pantalla de gráfica
class GraficaFrame(ctk.CTkFrame):
    def __init__(self, master, m, b):
        super().__init__(master)

        # título
        ctk.CTkLabel(self, text="Gráfica", font=("Arial", 18)).pack(pady=10)

        # obtener figura
        fig = gr.generar_grafica(m, b)

        # mostrar figura en tkinter
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()
        canvas.get_tk_widget().pack()

        # botón regresar
        ctk.CTkButton(self, text="Volver", command=lambda: master.cambiar_frame(Menu)).pack(pady=15)


# ejecutar
if __name__ == "__main__":
    app = App()
    app.mainloop()