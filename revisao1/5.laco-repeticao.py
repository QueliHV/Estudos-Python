'''
5. Laços de Repetição
	9.	Imprima os números de 1 a 10 usando for.
	10.	Some todos os números pares de 1 a 100 usando while.
'''

for num in range(1,11):
	print(num )

soma = 0
contador = 0

while(contador < 100):
    contador += 1
    if contador % 2 == 0:
        soma += contador
	
else:
    print(f'A soma de todos os pares é {soma}')		


    

