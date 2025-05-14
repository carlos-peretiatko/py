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

print("A quantidade total de ovelhas é", QtdeTotal)
print("O valor total é", VlrTotal)