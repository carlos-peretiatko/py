# (0 °C × 9/5) + 32 = 32 °F
# C = (F - 32) * 5/9.

print("Conversão de temperatura Celsius para Fahrenheit (1)" \
      "Conversão de temperatura Fahrenheit para Celsius (2)" \
      "Formulas para conversão manual (3)" \
      "Sair (0)")

opcao = int(input("Escolha uma opção: "))
match opcao:
    case 1: 
        celsius = float(input("Informe a temperatura em Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"A temperatura em Fahrenheit é: {fahrenheit:.2f} °F")
    case 2:
        fahrenheit = float(input("Informe a temperatura em Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"A temperatura em Celsius é: {celsius:.2f} °C")
    case 3: 
        print("Formulas para conversão manual:")
        print("Celsius para Fahrenheit: (C × 9/5) + 32 = F")
        print("Fahrenheit para Celsius: (F - 32) × 5/9 = C")
    case 0:
        print("Saindo do programa...")
    case _:
        print("Opção inválida. Tente novamente.")