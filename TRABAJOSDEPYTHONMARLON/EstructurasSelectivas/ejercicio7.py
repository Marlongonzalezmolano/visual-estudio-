#ejericicio de las llantas
print("descuentos en llantas todo terreno") #imprimo esto para que salga un titulo sobre lo que se trata 
llantas_Compradas=int (input("Cuantas llantas compro:"))# declaro la la cantidad de llantas comprada y hago que lo esciriba el usuario

if llantas_Compradas<5: # coloco una condicion que si las llantas compradas son menores que 5 tenga el siguiente proceso:
    print(f"Cada llanta te sale 300")# impirmo de que cada llanta le sale a 300
    Total_Compra= llantas_Compradas*300 #declaro la variable de total a pagar es igual a las llantas compradas por los 300 que le sale cada una 
    print(f"El total a pagar es  {Total_Compra}") #por ultimo hago que me imprima el total a pagar el usuario de la compra
elif llantas_Compradas<=10:#utilizo el elif para que la compra de las llantas sea menor que 10 o igual
    print(f"Cada llanta te sale a 250")# impirmo de que cada llanta le sale a 250
    Total_Compra=llantas_Compradas*250 #declaro la variable de total a pagar es igual a las llantas compradas por los 250 que le sale cada una 
    print(f"El total a pagar es  {Total_Compra}") #por ultimo hago que me imprima el total a pagar el usuario de la compra
elif llantas_Compradas>10:# utilizo el condicional elif y declaro de que si las llantas compradas son mayores que 10 haga los siguiente 
    print(f"Cada llanta te sale a 200")# impirmo de que cada llanta le sale a 200
    Total_Compra=llantas_Compradas*200  #declaro la variable de total a pagar es igual a las llantas compradas por los 200 que le sale cada una 
    print(f"El total a pagar es  {Total_Compra}") #por ultimo hago que me imprima el total a pagar el usuario de la compra




