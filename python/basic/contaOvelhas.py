vetCores = ["Branca", "Marrom", "Malhada"]
vetQtde = [3]
vetTotal = [3]
QtdeTotal = 0
VlrTotal = 0

# entrada de Dados

for i in range(len(vetQtde)):
    print("Informe a quantidade de ovelhas da cor", vetCores[i])
    vetQtde[i] = int(input())

    QtdeTotal += vetQtde[i]
    match vetCores[i]:
        case "Branca":
            VlrTotal += vetQtde[i] * 10
        case "Marrom":
            VlrTotal += vetQtde[i] * 20
        case "Malhada":
            VlrTotal += vetQtde[i] * 30
        case _:
            print("Cor inválida")
            len(vetCores) - 1
            break

    VlrTotal += vetQtde[i]

# saida de dados

print("COR \tQRDE \tTOTAL")
print("------------------")

for i in range(3):
    print(vetCores[i], "\t", vetQtde[i], "\t", vetTotal[i])

print("------------------")
print("Total de ovelhas: ", QtdeTotal)
print("Valor total: R$", VlrTotal)