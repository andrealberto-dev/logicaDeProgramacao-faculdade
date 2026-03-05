nota_prova = float(input("Digite a nota da prova: "))
nota_trabalho = float(input("Digite a nota do trabalho: "))

media = (nota_prova + nota_trabalho) / 2

if media >= 7:
    print(f"Sua média foi {media}, parabéns. Você está APROVADO!")
elif media >= 5:
    print(f"Sua média foi {media}, estude mais. Você está de RECUPERAÇÃO!")
else:
    print(f"Sua média foi {media}, melhore um pouco mais. Você está REPROVADO!")
