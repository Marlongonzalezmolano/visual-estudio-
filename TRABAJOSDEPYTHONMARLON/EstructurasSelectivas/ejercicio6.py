# programa para estimular a los almunos 
from random import * # abro una libreria 
Nom_alumno=str(input("ingrese el nombre del estudiante: ")) #declaro una varibale para que el usuario ponga el nombre del estudiante
Prom_Alumno=int(input("ingrese el promedio del estudiante en el ultimo perido: ")) # declaro otra variable para que ponga el promedio del del alumno 

if Prom_Alumno>=9: #coloco una condicion para que si el almuno saco 9 o mas haga un procedimiento 
    print("te toco un descuento del 30%")# impirmo el decuento obtenido por el alumno deacuerdo con el promedio 
    Pension=float(input("ingrese el pago de la pension: "))# declaro la la pension que el almuno tiene que pagar mensual y hago que el usuario la coloque 
    Valor_Pagar=Pension-(Pension*0.30) # declaro el valor a pagar y hago la siguiente operacion a la pension le reto la pension y el descuento 
    print (f"el total a pagar es: {Valor_Pagar}") #impirmo el total a pagar del estudiante y el resultado es de acuerdo a la operacion
elif Prom_Alumno<9: #coloco la condicion de elif para que si si el almuno saca menos de 9, haga lo siguiente:
    print("no te toco decuento") # imprimo de que no tiene descuento deacuerdo al promedio no le alcanza
    Pension=float(input("ingrese el pago de la pension: ")) # declaro la pension del estudiate que tiene que pagar mensual y hago de que la ingrese por medio del teclado
    IVA=0.10 #declaro de que IVA obtenido es de 10% que conviertiendolo da 0.10
    Valor_Pagar=Pension+(Pension*IVA) #decalro el valor a pagar es igual a la pension sumada con el apension del alumno mas el 0.10 del IVA
    print (f"el total a pagar es: {Valor_Pagar} Con el IVA del 10%") # hago que imprima el total a pagar y el IVA que ha obtenido 

