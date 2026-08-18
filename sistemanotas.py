# Criamos um dicionário de exemplo
aluno = {
    "nome": "Ana",
    "notas": [8.5, 7.0, 9.0]
}

def calcular_resultado(notas):
    media = sum(notas) / len(notas)
    if media >= 7.0:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"
    return media, situacao

def sistema_de_notas():
    turma = [] # Lista principal que vai guardar todos os dicionários de alunos

    while True:
        print("\n--- CADASTRO DE ALUNOS ---")
        nome = input("Nome do aluno: ").strip()

        notas = []
        for i in range(1, 4): 
            while True:
                try:
                    nota = float(input(f"Digite a {i}ª nota (0 a 10): "))
                    if 0 <= nota <= 10: 
                        notas.append(nota)
                        break
                    else:
                        print("Nota inválida! Digite um valor entre 0 e 10.")
                except ValueError:
                    print("Por favor, digite apenas número!")

        media, situacao = calcular_resultado(notas)

        # Montamos o dicionário do aluno e colocamos na lista 'turma'
        aluno = {
            "nome": nome,
            "notas": notas,
            "media": media,
            "situacao": situacao
        }
        turma.append(aluno)

        continuar = input("\nDeseja cadastrar outro aluno? (s/n): ").strip().lower()
        if continuar != 's':
            break  # Interrompe o while True principal do sistema

    # IMPRESSÃO DO RELATÓRIO FINAL
    print("\n" + "="*40)
    print("RELATÓRIO FINAL DA TURMA")
    print("="*40)
    for aluno in turma:
        print(f"Aluno: {aluno['nome']}")
        print(f"Notas: {aluno['notas']}")
        print(f"Média: {aluno['media']:.2f}")
        print(f"Situação: {aluno['situacao']}")
        print("-" * 30)

# Executa o sistema de notas
sistema_de_notas()