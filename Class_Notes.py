import os 
notas = []
soma = 0
nomes = []
gabarito = []

print("--------------------")
print("GABARITO")
print("--------------------")
for i in range(1,5+1):
    respostas = input (f"{i} Respostas: ")
    gabarito.append(respostas)
print("\n" * os.get_terminal_size().lines)

for i in range(1,3+1):
    print("----------------")
    print("ALUNOS",i)
    print("----------------")
    nome = input(f"Nome {i}: ")
    nomes.append(nome)
    nota = 0
    for j in range(1,5+1):
        questoes = input(f"questão {j}º")
        if questoes == gabarito[j-1]:
            nota = nota + 2
    notas.append(nota)
    print("\n" * os.get_terminal_size().lines)
print("----------------------")
print("TABELA GERAL")
print("----------------------")
print(nomes, notas)
soma_das_notas = sum(notas)
media = soma_das_notas/3
print(f"MEDIA DA TURMA: {media:.1f}")