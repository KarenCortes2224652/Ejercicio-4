# Ejercicio 4:
from sre_constants import CH_LOCALE
print("--------------")
print("--- CAJERO ---")
print("--------------")

#Input
TB1 = 0
TB2 = 0
TB3 = 0
CH = int

#Processing
while CH != 0:
    CH = int(input("\nDigita el valor del cheque: "))
    B1 = CH // 10000
    B2 = (CH - (B1 * 10000)) // 2000
    M = (CH - (B1 * 10000) - (B2 * 2000)) // 100
    print("\nPara el cheque de: " + str(CH) + "se entregan: \n " + str(B1) + "Billetes de 10.000; " + str(B2) + "Billetes de 2.000 y  " + str(M) + "Monedas de 100 ")

    TB1 = TB1 + B1
    TB2 = TB2 + B2
    TB3 = TB3 + M
    print("\nEn el transcurso de el día se entregaron: \n" + str(TB1) + " Billetes de 10.000; " + str(TB2) + "Billetes de 2.000 y " + str(TB3) + "Monedas de 100 ")

