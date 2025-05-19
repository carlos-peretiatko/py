# O índice é calculado da seguinte maneira: divide-se o peso do paciente pela sua altura elevada ao quadrado.
# Diz-se que o indivíduo tem peso normal quando o resultado do IMC está entre 18,5 e 24,9.

# Menor que 18,5  	    Magreza	
# Entre 18,5 e 24,9   	Normal	
# Entre 25,0 e 29,9	    Sobrepeso	
# Entre 30,0 e 39,9	    Obesidade	
# Maior que 40,0	    Obesidade Grave


altura = float(input("Informe a altura do paciente (em metros): "))

if altura <= 0:
    print("Altura inválida. Deve ser maior que zero.")
    exit()

peso = float(input("Informe o peso do paciente (em kg): ")) 

if peso <= 0:
    print("Peso inválido. Deve ser maior que zero.")
    exit()

imc = peso / (altura ** 2)

if imc < 18.5:
    classificacao = "Magreza"
elif 18.5 <= imc < 25:
    classificacao = "Normal"
elif 25 <= imc < 30:
    classificacao = "Sobrepeso"
elif 30 <= imc < 40:
    classificacao = "Obesidade"
else:
    classificacao = "Obesidade Grave"

print(f"IMC: {imc:.2f}") # Formata o IMC com duas casas decimais
print("Sua classificação é:", classificacao) 