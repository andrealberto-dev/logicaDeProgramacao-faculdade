print("Olá, eu sou a sua assistente de Python. O que você quer fazer hoje ?")

comando = input("Digite um comando: ")

match comando:
    case "oi" | "olá":
        print("Oi, como vai você?")
    case "tchau" | "sair" | "fim" | "exit":
        print("Tchau, foi bom conversar com você!")
    case "piada":
        print("Sabe qual é o rei da geladeira ? O requeijão 🤣😁")
    case "clima" | "previsão do tempo":
        print("Tá muuuuuuuuito quente!!! Deve ter passado de 38°C! 🥵")
    case _:
        print("Desculpe, não entendi o comando.")
