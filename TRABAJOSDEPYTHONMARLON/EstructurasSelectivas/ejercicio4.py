color = str(input("digite un color :")) # declaro la variable y hago que el usuario ingrese el color
compra =float(input("digite el valor de la compra")) # declaro compra como float ya que podemos utilizar decimales en este 

if color =="rojo": # aplico un condicional para tomar una desicion que si el color es rojo me lleve a el siguiente proceso:
    descuento =compra*0.15 # declaro descuento es igual a la compra por el 15 porciento del total de la compra
    valorPagar=compra-descuento #declaro valor a pagar menos la compra menos el decunto 
    print("El valor de la compra fue:",compra,"usted saco la balota: ",color,"con un descuento de:",descuento,"el valor a pagar es:",valorPagar)# hago que imprima todo deacuerdo a lo que el cliente ponga imprimira el color , decuento, y el valor a pagar
    
elif color == "verde": #utilizo una condicion y aqui si da el color verde hace la siguiete funcion:
    descuento= compra*0.20 # declaro del descuento que sea igual a la compra por el porcentaje del 20%
    valorPagar=compra-descuento # declaro el valor a pagar sea igual a compra menos el descuento aplicado 
    print("El valor de la compra fue:",compra,"usted saco la balota: ",color,"con un descuento de:",descuento,"el valor a pagar es:",valorPagar) # hago que imprima todo deacuerdo a lo que el cliente ponga imprimira el color , decuento, y el valor a pagar
else:
    print("no tienes descuento") #y si no cumple la funcion no tiene descuento 

