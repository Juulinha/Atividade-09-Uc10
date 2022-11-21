#calculadora de pesos ideais

sexo = input("Digite seu sexo: ")
h = float(input("Digite sua altura: "))
pm = (72.7*h)- 58
pf = (62.1*h) - 44.7

print("Sexo: ", sexo)
if sexo == "feminino":
    print("Digite sua altura", h, "cm")
    print("Peso feminino: ", pf)
elif sexo == "masculino":
    print("Digite sua altura", h, "cm")
    print("Peso masculino: ", pm)





