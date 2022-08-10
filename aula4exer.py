# print("Dia\tMês\tAno\n01\t01\t2019")

# entrada=input('digite um numero')
# saida = entrada*3
# print('Saida: ', saida)

nome=input('digite o nome')
altura=float(input('digite a altura'))
peso=float(input('digite o peso'))

alturaq =float(altura * altura)
imc = float(peso/alturaq)
print(imc)