horas = float(input("Introduce tus horas de trabajo: "))
coste = float(input("Introduce lo que cobras por horas: "))
extra = input("Ingrese las horas extras: ")
extra = int(extra)
h_extra = (extra * coste)
paga = (horas * coste) + h_extra
print("Tu paga es", paga)
