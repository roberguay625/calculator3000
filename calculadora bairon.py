print("que quieres hacer maricon?")

pregunta = input("Sumar, resta, multiplicar, dividir")

numero1 = int(input("mete un numero negro"))

numero2 = int(input("mete otro numero negro"))

def sumar (num1, num2): 
    return num1 + num2

def multiplicar (num1, num2):
    return (num1 * num2)

def dividir (num1, num2):
    return num1 / num2

def restar (num1, num2):
    return num1 - num2

if pregunta == "Sumar":
   print(sumar (numero1, numero2))

elif pregunta == "Restar":
    print(restar (numero1, numero2))

elif pregunta == "Dividir":
    print(dividir (numero1, numero2))

elif pregunta == "Multiplicar":
    print(multiplicar (numero1, numero2))

else:
    print("tu que eres tonto")
