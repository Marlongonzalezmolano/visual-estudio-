CantidadDeZapatillas= int(input("ingrese la cantidad de zapatillas compradas: ")) #aca declaramos para que el usuario ingrese la cantidad de zapatillas compradas
ValorUnitario= int(input("ingrese el total a pagar por las zapatillas: "))# despues que el cliente ingrese el valor unitario de cada zaptilla comprada 
subTotal= CantidadDeZapatillas*ValorUnitario # despues declaramos la vairbale subTotal y hacemos la multiplicacion de la cantidad de las zapatillas por el valor unitario de estas 

if CantidadDeZapatillas>=3: #aca hacemos una desicion en el cual si la cantidaddeZapatillas es mayor o igual a 3 tire la siguiente operacion
    totalaPagar= subTotal-(subTotal*0.20)  #aca declaramos totalPagar y ahcemos la siguietne porecion subTotal lo testamos por el SubTotal y el descuento que se le aplica del 20%
    print(f"el total a pagar con su descuento del 20% es:{totalaPagar} " ) # impirmimos la cantidad apagar el cliente deacuerdo con lo que halla dado en la operacion
elif CantidadDeZapatillas<3: # sino que tome la siguiente desicion que es si compra menos de 3 zapatillas 
   totalaPagar2 = subTotal-(subTotal*0.10) # declaramos un segundo totalaPagar2 que hacemos la siguiente operacion al subTotal lo restamos por el subTotal y el descuento apliacdo del 10%
   print(f"Total a pagar con el descuento del 10% es:{totalaPagar2} ") #y que hgaga que le imprime el el tipo de descuento recibido y el total de lo que tenga que pagar 