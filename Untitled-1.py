def Multiplicacion():
    resultado = chokko * wafle
    print(resultado)
def Division():
    resultado = chokko / wafle
    print(resultado)
def Suma():
    resultado = chokko + wafle
    print(resultado)
def Resta():
    resultado = chokko - wafle
    print(resultado)


     
print("Calculadora")
chokko = float(input("Ingrese el primer valor: "))
Monoko = input("Ingrese el operador: ")
wafle = float(input("Ingrese el segundo valor: "))
if Monoko == "*":
    Multiplicacion()
if Monoko == "/":
    if wafle == 0:
        print("No se divide entre 0")
        exit
    else:
       Division() 
if Monoko == "+":
    Suma()
if Monoko == "-":
    Resta()