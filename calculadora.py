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