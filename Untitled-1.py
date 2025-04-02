def Calculadora():
    def Multiplicacion():
        resultado = chokko * wafle
        print(resultado)
    def Division():
        resultado = chokko/wafle if wafle != 0 else "No se puede dividir entre cero"
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
        Division() 
    if Monoko == "+":
        Suma()
    if Monoko == "-":
        Resta()
    respuesta = input("Desea continuar calculando si o no? ")
    if respuesta == "si":
        Calculadora()
    if respuesta == "no":
        print("Se cierra la calculadora")
Calculadora()