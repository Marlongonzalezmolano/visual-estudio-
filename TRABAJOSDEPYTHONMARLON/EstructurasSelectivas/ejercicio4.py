color = str(input("digite un color :")) # declaro la variable y hago que el usuario ingrese el color
compra =float(input("digite el valor de la compra")) # declaro compra como float ya que podemos utilizar decimales en este 

if color =="rojo": # aplico un condicional para tomar una desicion que si el color es rojo me lleve a el siguiente proceso:
    descuento =compra*0.15 # declaro descuento es igual a la compra por el 15 porciento del total de la compra
    valorPagar=compra-descuento
    print("El valor de la compra fue:",compra,"usted saco la balota: ",color,"con un descuento de:",descuento,"el valor a pagar es:",valorPagar)
    
elif color == "verde":
    descuento= compra*0.20
    valorPagar=compra-descuento
    print("El valor de la compra fue:",compra,"usted saco la balota: ",color,"con un descuento de:",descuento,"el valor a pagar es:",valorPagar)
else:
    print("no tienes descuento")

