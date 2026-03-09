soma = 0
num = 1

# while num <= 10:
#    soma = soma + num
#    num = num + 1

for index in range(1, 11):
    soma += index

# soma = sum([i for i in range(1,11)]) - Array

print(f"A soma dos números de 1 a 10 é {soma}")