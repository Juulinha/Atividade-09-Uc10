#Calculadora de exceção de quilos de peixes

pei = float(input("Digite a quantidade de peixes em quilos: "))
exc = float(input("Digite o excesso de quilos de peixes: "))
val = 4.00 
mul = exc * val


if pei <= 50 and exc ==0:
    print("sua pesca não excedeu o peso máximo")
    print("peso: ", pei, "KG")
    print("excesso: ", exc)
    print("multa: ", mul)
else:
    print("sua pesca excedeu o peso máximo")
    print("peso: ", pei, "KG")
    print("excesso: ", exc)
    print("multa: ", mul)