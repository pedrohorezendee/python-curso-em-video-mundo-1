nome = 'Pedro Rezende'
altura = 1.90
peso = 116
imc = peso / (altura * altura)


"f-strings"
linha_1 = f'{nome} tem {altura:.2f} de altura' #(:.2f) -> remetendo a 2 casas decimais 
linha_2 = f'pesa {peso} quilos e seu IMC é'
linha_3 = f'{imc:.2f}'

# Pedro Rezende tem 1.90 de altura,
# pesa 116 quilos e seu IMC é 
#32,13296398891967

print(linha_1)
print(linha_2)
print(linha_3)
