monto= float (input("ingrese el total de la compra: ")) #primero declaro la variable monto que es la compra que se esta haciendo a los bolsos 

 
if monto>50000: #utilizamos la funcion if para poner monto y de ahi si es mayor que $500.000 va hacia un camino
  
  compraFinal= (monto*0.55) #capa declaramos la compra final de la compra y ponemos el monto de la plata y lo multiplicamos por el 55% del propio dinero de la empresa 
  prestamo_banco= (monto*0.30) #para saber el total del prestamo del banco al monto lo multiplicamos por el 30% del prestamo del banco 
  creditoFabricante = (monto*0.20) #declaramos variable del credito del fabricante y al monto del dinero que hay que pagar lo multiplicamos por el 20% de intreses 
else:
   monto<=50000 #hacemos una compracion de que si el dinero es menor de $500.000 o igual tire la siguiente funcion:
   compraFinal= monto+(monto*0.70*0.30) #declaramos la compraFinal y a esta el monto del dinero se le suma el monto multiplicado por el 70% del dinero propio y tambien el 30% de la solicitud del fabricante 
   creditoFabricante=(monto*0.30)+(monto*0.20) #para ultimo declaramos el credito del fabricante y a esta varibale lo ponemos el monto de lo mutiplicamos por el 20% sobre los intereses
   prestamo_banco=0 #declaramos el prestamo_banco es igual a cero ya que gracias a que el monto es menos a $500.000 no le pedimos prestamo al banco  

print("la empresainvirtio invirtio", compraFinal, "le solicito restado al banco", prestamo_banco,"el valor solicitado del credito del fabricante fue de: ", creditoFabricante)
 # por ultimo impimimos todo de acuerdo con la compra para que salga el enuniciado final de acuerdo a todo lo echo anterior mente
