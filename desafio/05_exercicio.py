# %%
notas = input("Digite as 3 notas separadas por vírgula (por exemplo: 8, 7.5, 9)")

lista_notas = notas.split(",")
nota1 = float(lista_notas[0].strip())
nota2 = float(lista_notas[1].strip())
nota3 = float(lista_notas[2].strip())

media = (nota1 + nota2 + nota3) // 3
aprovado = media > 6.0

print("Média: ", media)
print("Aprovado(a): ", aprovado)

# %%