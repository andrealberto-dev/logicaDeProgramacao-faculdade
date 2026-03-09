print("-=-" * 8)
print("! Calculadora de Notas !")
print("-=-" * 8)

nota1 = int(input("Nota da prova: "))
nota2 = int(input("Nota do trabalho: "))
nota3 = int(input("Nota da avaliação: "))

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print("PARABÉNS! Você passou!")
elif media < 5:
    print("QUE PENA! Você não passou!")
else:
    print("ESTUDE MAIS! Você está de recuperação!")
