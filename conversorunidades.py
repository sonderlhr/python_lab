CONVERSOES_COMPRIMENTO = {
    "metro": 1.0,
    "quilometro": 0.001,
    "centimetro": 100.0,
    "milimetro": 1000.0,
    "milha": 0.000621371,
    "pe": 3.28084
}

def converter_comprimento(valor, unidade_origem, unidade_destino):
    valor_em_metros = valor / CONVERSOES_COMPRIMENTO[unidade_origem]
    return valor_em_metros * CONVERSOES_COMPRIMENTO[unidade_destino]

def executar_conversor():
    while True:
        print("n=== CONVERSOR DE UNIDADES ===")
        print("Unidades disponíveis:",",".join(CONVERSOES_COMPRIMENTO.keys()))
        print("Digite 'sair' a qualquer momento para encerrar.")

        origem = input("/n Converter de : ").strip().lower()
        if origem == 'sair':
            break

        destino = input("Para: ").strip().lower()
        if destino == 'sair':
            break

        if origem not in CONVERSOES_COMPRIMENTO or destino not in CONVERSOES_COMPRIMENTO:
            print("/n Erro: Uma ou ambas as unidades são inválidas. Tente novamente.")
            continue

        try: 
            valor = float(input(f"Digite o valor em {origem}: "))
            resultado = converter_comprimento(valor, origem, destino)
            print(f"/n Resposta: {valor} {origem} = {resultado:.4f} {destino}")
        except ValueError:
            print("/n Erro: Por favor, digite um número válido.")

executar_conversor()