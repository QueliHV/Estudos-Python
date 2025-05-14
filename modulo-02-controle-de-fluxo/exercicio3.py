#3.	Use for para exibir os números pares entre 1 e 20.

for number in range(1, 21):  # Não considera o ultimo numero
    if number % 2 == 0:
        print(number)
    