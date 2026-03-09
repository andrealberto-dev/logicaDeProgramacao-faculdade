print("-=-" * 16)
print("Bem vindo ao DETRAN!")
print("Este é o novo sistema para liberar ou não a CNH")
print("-=-" * 16)
print()

idade = int(input("Digite a sua idade: "))

if idade >= 18:
    print("Você ESTÁ liberado para ter CNH!")
else:
    print("Você NÃO está liberado para ter CNH!")
