genero = str(input("Em que turno voce estuda ? : [M, T ou N]: "))

if genero == "m" or genero == "M":
    print("M -Voce estuda pela manha")
elif genero == "T" or genero == "t":
    print("T - Voce estuda pela tarde")
elif genero == "N" or genero =="n":
     print("N - Voce estuda pela noite")
else:
    print("VOCE NAO ESTUDA EM NENHUM TURNO")