<<<<<<< HEAD
def calcular(numero1, numero2, operacao):
    if operacao == "+":
        return numero1 + numero2

    elif operacao == "-":
        return numero1 - numero2

    elif operacao == "*":
        return numero1 * numero2

    elif operacao == "/":
        if numero2 == 0:
            return "Erro"
        return numero1 / numero2

    return "Operação inválida"
=======
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

operacao = input("Digite a operação (+. -, *, /): ")

if operacao == "+":
    resultado = numero1 + numero2
elif operacao == "-":
    resultado = numero1 - numero2
elif operacao == "*":
    resultado = numero1 * numero2
else:
    resultado = numero1 / numero2

print( f"Resultado: {resultado}")    
>>>>>>> a797ed1d67d9df4b4bb5eea2d976f3dce5036440
