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
    try:
        chokko = float(input("Ingrese el primer valor: ")) 
    except ValueError as e: 
        try:
             Monoko = input("Ingrese el operador: ")
        except ValueError as e:
            try:         
                wafle = float(input("Ingrese el segundo valor: "))
            except ValueError as e:
                print('Los datos ingresados no son numeros.')
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