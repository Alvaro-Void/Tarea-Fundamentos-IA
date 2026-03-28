import tkinter as tk
from tkinter import messagebox

# listas
trabajadores = []
visitantes = []
compras = []
intentos_global = []

# funciones

def calcular_aumento(sueldo):
    if sueldo < 4000:
        return sueldo * 0.15
    elif sueldo <= 7000:
        return sueldo * 0.10
    else:
        return sueldo * 0.08

# 1
def sistema_sueldos():
    v = tk.Toplevel()
    v.title("Sueldos")

    nombre = tk.Entry(v)
    sueldo = tk.Entry(v)

    tk.Label(v, text="Nombre").pack()
    nombre.pack()
    tk.Label(v, text="Sueldo").pack()
    sueldo.pack()

    def guardar():
        try:
            n = nombre.get()
            s = float(sueldo.get())
            nuevo = s + calcular_aumento(s)
            trabajadores.append((n, nuevo))
            messagebox.showinfo("Resultado", nuevo)
        except:
            messagebox.showerror("Error", "Datos inválidos")

    def historial():
        texto = "\n".join([f"{t[0]}: {t[1]}" for t in trabajadores])
        messagebox.showinfo("Historial", texto or "Vacío")

    tk.Button(v, text="Calcular", command=guardar).pack()
    tk.Button(v, text="Historial", command=historial).pack()

# 2
def sistema_parque():
    v = tk.Toplevel()
    v.title("Parque")

    nombre = tk.Entry(v)
    edad = tk.Entry(v)
    juegos = tk.Entry(v)

    tk.Label(v, text="Nombre").pack()
    nombre.pack()
    tk.Label(v, text="Edad").pack()
    edad.pack()
    tk.Label(v, text="Juegos").pack()
    juegos.pack()

    def calcular():
        try:
            e = int(edad.get())
            j = int(juegos.get())
            total = j * 50

            if e < 10:
                total *= 0.75
            elif e <= 17:
                total *= 0.90

            visitantes.append(total)
            messagebox.showinfo("Total", total)
        except:
            messagebox.showerror("Error", "Datos inválidos")

    def total():
        messagebox.showinfo("Recaudado", sum(visitantes))

    tk.Button(v, text="Calcular", command=calcular).pack()
    tk.Button(v, text="Total", command=total).pack()

# 3
def sistema_tienda():
    v = tk.Toplevel()
    v.title("Tienda")

    nombre = tk.Entry(v)
    mes = tk.Entry(v)
    importe = tk.Entry(v)

    tk.Label(v, text="Cliente").pack()
    nombre.pack()
    tk.Label(v, text="Mes").pack()
    mes.pack()
    tk.Label(v, text="Importe").pack()
    importe.pack()

    def calcular():
        try:
            m = mes.get().lower()
            imp = float(importe.get())

            if m == "octubre":
                imp *= 0.85
            elif m == "diciembre":
                imp *= 0.80
            elif m == "julio":
                imp *= 0.90

            compras.append(imp)
            messagebox.showinfo("Total", imp)
        except:
            messagebox.showerror("Error", "Datos inválidos")

    def total():
        messagebox.showinfo("Total vendido", sum(compras))

    tk.Button(v, text="Calcular", command=calcular).pack()
    tk.Button(v, text="Total día", command=total).pack()

# 4
def validar_menor_10():
    v = tk.Toplevel()
    v.title("<10")

    intentos = []
    e = tk.Entry(v)
    e.pack()

    def validar():
        try:
            n = int(e.get())
            intentos.append(n)
            if n < 10:
                messagebox.showinfo("Correcto", f"{n} Intentos: {len(intentos)}")
            else:
                messagebox.showerror("Error", "Mayor o igual a 10")
        except:
            messagebox.showerror("Error", "Inválido")

    tk.Button(v, text="Validar", command=validar).pack()

# 5
def validar_rango():
    v = tk.Toplevel()
    v.title("Rango 0-20")

    e = tk.Entry(v)
    e.pack()

    def validar():
        try:
            n = int(e.get())
            if 0 < n < 20:
                messagebox.showinfo("Correcto", n)
            else:
                messagebox.showerror("Error", "Fuera de rango")
        except:
            messagebox.showerror("Error", "Inválido")

    tk.Button(v, text="Validar", command=validar).pack()

# 6
def validar_historial():
    v = tk.Toplevel()
    v.title("Historial")

    e = tk.Entry(v)
    e.pack()

    def validar():
        try:
            n = int(e.get())
            intentos_global.append(n)
            if 0 < n < 20:
                messagebox.showinfo("Correcto", n)
            else:
                messagebox.showerror("Error", "Incorrecto")
        except:
            messagebox.showerror("Error", "Inválido")

    def mostrar():
        errores = len([x for x in intentos_global if not (0 < x < 20)])
        messagebox.showinfo("Historial", f"Intentos: {intentos_global}\nErrores: {errores}")

    tk.Button(v, text="Validar", command=validar).pack()
    tk.Button(v, text="Historial", command=mostrar).pack()

# 7
def suma_n():
    v = tk.Toplevel()
    v.title("Suma N")

    e = tk.Entry(v)
    e.pack()

    def calc():
        try:
            n = int(e.get())
            if n <= 0:
                raise
            lista = list(range(1, n+1))
            messagebox.showinfo("Resultado", f"{lista}\n{sum(lista)}")
        except:
            messagebox.showerror("Error", "Inválido")

    tk.Button(v, text="Calcular", command=calc).pack()

# 8
def suma_acumulada():
    v = tk.Toplevel()
    v.title("Acumulada")

    lista = []
    e = tk.Entry(v)
    e.pack()

    def agregar():
        try:
            n = int(e.get())
            if n == 0:
                messagebox.showinfo("Final", f"{lista}\nTotal: {sum(lista)}")
            else:
                lista.append(n)
                messagebox.showinfo("Suma", sum(lista))
        except:
            messagebox.showerror("Error", "Inválido")

    tk.Button(v, text="Agregar", command=agregar).pack()

# 9
def suma_hasta_100():
    v = tk.Toplevel()
    v.title(">100")

    lista = []
    e = tk.Entry(v)
    e.pack()

    def agregar():
        try:
            n = int(e.get())
            lista.append(n)
            s = sum(lista)
            messagebox.showinfo("Suma", s)
            if s > 100:
                messagebox.showinfo("Final", f"{lista}\n{s}")
        except:
            messagebox.showerror("Error", "Inválido")

    tk.Button(v, text="Agregar", command=agregar).pack()

# 10
def pago_trabajadores():
    v = tk.Toplevel()
    v.title("Pagos")

    nombre = tk.Entry(v)
    hn = tk.Entry(v)
    ph = tk.Entry(v)
    he = tk.Entry(v)
    hijos = tk.Entry(v)

    for txt, ent in [("Nombre", nombre),("Horas normales", hn),("Pago hora", ph),("Horas extra", he),("Hijos", hijos)]:
        tk.Label(v, text=txt).pack()
        ent.pack()

    datos = []

    def calc():
        try:
            n = nombre.get()
            hnorm = float(hn.get())
            pago = float(ph.get())
            hextra = float(he.get())
            h = int(hijos.get())

            total = (hnorm * pago) + (hextra * pago * 1.5) + (h * 0.5)
            datos.append((n, total))
            messagebox.showinfo("Pago", total)
        except:
            messagebox.showerror("Error", "Datos inválidos")

    def reporte():
        texto = "\n".join([f"{d[0]}: {d[1]}" for d in datos])
        messagebox.showinfo("Reporte", texto or "Vacío")

    tk.Button(v, text="Calcular", command=calc).pack()
    tk.Button(v, text="Reporte", command=reporte).pack()

# menu
def main():
    root = tk.Tk()
    root.title("Menú")

    botones = [
        ("1. Sueldos", sistema_sueldos),
        ("2. Parque", sistema_parque),
        ("3. Tienda", sistema_tienda),
        ("4. <10", validar_menor_10),
        ("5. Rango", validar_rango),
        ("6. Historial", validar_historial),
        ("7. Suma N", suma_n),
        ("8. Acumulada", suma_acumulada),
        ("9. >100", suma_hasta_100),
        ("10. Pagos", pago_trabajadores)
    ]

    for txt, cmd in botones:
        tk.Button(root, text=txt, command=cmd).pack(fill="x")

    root.mainloop()

if __name__ == "__main__":
    main()
