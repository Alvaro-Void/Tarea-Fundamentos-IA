import customtkinter as ctk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tkinter import messagebox

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

# cargar archivo
try:
    df = pd.read_csv("master.csv")
    df.columns = df.columns.str.strip()

    # limpiar columna de GDP
    df["gdp_for_year ($)"] = df["gdp_for_year ($)"].astype(str).str.replace(",", "").astype(float)

    # rellenar HDI con promedio por año y luego general
    df["HDI for year"] = df.groupby("year")["HDI for year"].transform(lambda x: x.fillna(x.mean()))
    df["HDI for year"] = df["HDI for year"].fillna(df["HDI for year"].mean())

    # seleccionar países principales
    top_paises = df.groupby("country")["suicides_no"].sum().sort_values(ascending=False).head(12).index
    df_filtrado = df[df["country"].isin(top_paises)]

except:
    df = None

archivo_users = "usuarios.txt"

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Sistema")
        self.geometry("1100x650")
        self.login()

    def clear(self):
        for w in self.winfo_children():
            w.destroy()

    # pantalla de login
    def login(self):
        self.clear()
        frame = ctk.CTkFrame(self)
        frame.pack(pady=100)

        self.user = ctk.CTkEntry(frame, placeholder_text="Usuario")
        self.user.pack(pady=5)

        self.passw = ctk.CTkEntry(frame, placeholder_text="Contraseña", show="*")
        self.passw.pack(pady=5)

        ctk.CTkButton(frame, text="Ingresar", command=self.validar_login).pack(pady=10)

    # validar usuario
    def validar_login(self):
        try:
            with open(archivo_users) as f:
                for linea in f:
                    u, p = linea.strip().split(",")
                    if self.user.get() == u and self.passw.get() == p:
                        self.menu()
                        return
            messagebox.showerror("Error", "Login incorrecto")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    # menú principal
    def menu(self):
        self.clear()

        left = ctk.CTkFrame(self, width=250)
        left.pack(side="left", fill="y")

        self.right = ctk.CTkFrame(self)
        self.right.pack(side="right", expand=True, fill="both")

        for i in range(1,11):
            ctk.CTkButton(left, text=f"Consulta {i}", command=lambda x=i: self.consulta(x)).pack(pady=5, fill="x")

    # función para graficar
    def graficar_barras(self, data, titulo, ylabel):
        plt.figure(figsize=(12,5))

        data = data.sort_values()
        categorias = data.index.astype(str)
        valores = data.values

        plt.bar(categorias, valores)

        media = np.mean(valores)
        mediana = np.median(valores)
        std = np.std(valores)

        # líneas de referencia
        plt.axhline(media, color='red', linestyle='--', label=f"Media={media:.1f}")
        plt.axhline(mediana, color='green', linestyle='--', label=f"Mediana={mediana:.1f}")
        plt.axhline(media + std, color='purple', linestyle='--', label=f"+Desv={std:.1f}")
        plt.axhline(media - std, color='purple', linestyle='--')

        plt.title(titulo)
        plt.xlabel("Países")
        plt.ylabel(ylabel)

        plt.xticks(rotation=45, ha='right')
        plt.legend()
        plt.grid(True, alpha=0.3)

        plt.tight_layout()
        plt.show()

    # consultas
    def consulta(self, n):
        try:
            if n == 1:
                res = df_filtrado.groupby("country")["suicides/100k pop"].mean()
                self.graficar_barras(res, "Tasa promedio de suicidio por país", "Tasa")

            elif n == 2:
                res = df_filtrado.groupby("country")["suicides_no"].sum()
                self.graficar_barras(res, "Total de suicidios por país", "Suicidios")

            elif n == 3:
                res = df_filtrado.groupby("country")["suicides_no"].mean()
                self.graficar_barras(res, "Promedio de suicidios por país", "Promedio")

            elif n == 4:
                jovenes = df_filtrado[df_filtrado["age"].str.contains("15-24")]
                res = jovenes.groupby("country")["suicides_no"].sum()
                self.graficar_barras(res, "Suicidios en jóvenes por país", "Cantidad")

            elif n == 5:
                res = df_filtrado.groupby("country")["population"].sum()
                self.graficar_barras(res, "Población total por país", "Población")

            elif n == 6:
                res = df_filtrado.groupby("country")["gdp_per_capita ($)"].mean()
                self.graficar_barras(res, "PIB per cápita promedio por país", "PIB")

            elif n == 7:
                res = df_filtrado.groupby("country")["suicides/100k pop"].std()
                self.graficar_barras(res, "Variabilidad de tasa de suicidio", "Desviación")

            elif n == 8:
                res = df_filtrado.groupby("country")["suicides_no"].max()
                self.graficar_barras(res, "Máximo de suicidios registrados", "Suicidios")

            elif n == 9:
                pivot = df_filtrado.pivot_table(values="suicides_no", index="country", columns="sex", aggfunc="sum").fillna(1)
                res = pivot["male"] / pivot["female"]
                self.graficar_barras(res, "Relación hombres/mujeres", "Relación")

            elif n == 10:
                res = df_filtrado.groupby(["country","age"])["suicides_no"].sum().groupby(level=0).max()
                self.graficar_barras(res, "Concentración por edad en cada país", "Suicidios")

        except Exception as e:
            messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    app = App()
    app.mainloop()