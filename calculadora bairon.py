print("que quieres hacer maricon?")

pregunta = input("Sumar, restar, multiplicar, dividir: ").lower()

numero1 = int(input("mete un numero negro: "))

numero2 = int(input("mete otro numero negro: "))

def sumar (num1, num2): 
    return num1 + num2

def multiplicar (num1, num2):
    return (num1 * num2)

def dividir (num1, num2):
    return num1 / num2

def restar (num1, num2):
    return num1 - num2

if pregunta == "sumar":
   print(sumar(numero1, numero2))

elif pregunta == "restar":
    print(restar(numero1, numero2))

elif pregunta == "dividir":
    print(dividir(numero1, numero2))

elif pregunta == "multiplicar":
    print(multiplicar(numero1, numero2))

else:
    print("tu que eres tonto?")
