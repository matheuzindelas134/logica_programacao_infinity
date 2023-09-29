numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("digite o terceiro número: "))

if numero1 > numero2 and numero1 > numero3: 
    print(f"O {numero1 or numero2} é maior que o {numero3}")
elif numero2 or numero3 > numero1:
    print(f"O {numero2 or numero3} é maior que o {numero1}")
else:
    print("Os números são iguais")