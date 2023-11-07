from tkinter import Tk, Button, Entry

# Configuración ventana principal
root = Tk()
root.title("calculadora")
root.resizable(0,0)
root.geometry("")

# Configuración pantalla de salida 
pantalla = Entry(root, width=40, bg="black", fg="white", borderwidth=0, font=("arial", 18, "bold"))
pantalla.grid(row=0, column=0, columnspan=4, padx=1, pady=1)

#configuracion eventos
numeros = []
operadores = []
def imprimirNumero(x):
    if "/*+-".count(pantalla.get())==1:
        pantalla.delete(0,"end")
    pantalla.insert(50,x)

def imprimirOperador(y):
    numeros.append(float(pantalla.get()))
    operadores.append(y)
    pantalla.delete(0,"end")
    pantalla.insert(0,y)

def operaciones(operador,n):
    numeros.append(float(pantalla.get()))
    pantalla.delete(0,"end")
    resultado = 0
    if operadores[0] == "+":
        resultado = numeros[0]+numeros[1]
    elif operadores[0] == "-":
        resultado = numeros[0]-numeros[1]
    elif operadores[0] == "/":
        resultado = numeros[0]/numeros[1]
    elif operadores[0] == "*":
        resultado = numeros[0]*numeros[1]
    pantalla.insert(0,resultado)
# Configuración botones
boton_1 = Button(root, text="1", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command= lambda:imprimirNumero(1)).grid(row=1, column=0, padx=1, pady=1,sticky="ew")
boton_2 = Button(root, text="2", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command= lambda:imprimirNumero(2)).grid(row=1, column=1, padx=1, pady=1,sticky="ew")
boton_3 = Button(root, text="3", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command= lambda:imprimirNumero(3)).grid(row=1, column=2, padx=1, pady=1,sticky="ew")
boton_4 = Button(root, text="4", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command= lambda:imprimirNumero(4)).grid(row=2, column=0, padx=1, pady=1,sticky="ew")
boton_5 = Button(root, text="5", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command= lambda:imprimirNumero(5)).grid(row=2, column=1, padx=1, pady=1,sticky="ew")
boton_6 = Button(root, text="6", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command= lambda:imprimirNumero(6)).grid(row=2, column=2, padx=1, pady=1,sticky="ew")
boton_7 = Button(root, text="7", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command= lambda:imprimirNumero(7)).grid(row=3, column=0, padx=1, pady=1,sticky="ew")
boton_8 = Button(root, text="8", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command= lambda:imprimirNumero(8)).grid(row=3, column=1, padx=1, pady=1,sticky="ew")
boton_9 = Button(root, text="9", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command= lambda:imprimirNumero(9)).grid(row=3, column=2, padx=1, pady=1,sticky="ew")
boton_igual = Button(root, text="=", width=20, height=3, bg="red", fg="white", borderwidth=0, cursor=" hand2", command= lambda:operaciones(operadores,numeros)).grid(row=4, column=0, columnspan=2, padx=1, pady=1,sticky="ew")
boton_punto = Button(root, text=".", width=9, height=3, bg="spring green", fg="black", cursor="hand2", borderwidth=0,command=lambda: imprimirNumero(".")).grid(row=4, column=2, padx=1, pady=1,sticky="ew")
boton_mas = Button(root, text="+", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command=lambda: imprimirOperador("+")).grid(row=1, column=3, padx=1, pady=1,sticky="ew")
boton_menos = Button(root, text="-", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2",command= lambda: imprimirOperador("-")).grid(row=2, column=3, padx=1, pady=1,sticky="ew")
boton_multiplicacion = Button(root, text="*",  width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command= lambda: imprimirOperador("*")).grid(row=3, column=3, padx=1, pady=1,sticky="ew")
boton_division = Button(root, text="/", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command= lambda: imprimirOperador("/")).grid(row=4, column=3, padx=1, pady=1,sticky="ew")

root.mainloop()