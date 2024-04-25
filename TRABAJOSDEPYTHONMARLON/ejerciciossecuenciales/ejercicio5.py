#precio final de una compra
ValorCompra= int(input ("ingrese el valor de la compra: "))
#declaramos la variable ValorCompra con int para dar el resultado numerico de la compra realizada
Descuento= int(input ("ingrese el descuento: "))
#declaramos varibale de decuento a realizar a la compra 
Descuento= Descuento/100
#para hallar el decuento toca dividir el decuento en 100 
PrecioDescuento= ValorCompra*Descuento
#despues para saber el descuento de la compra multiplicamos ValorCompra por el descuento 
Preciofianl= ValorCompra-PrecioDescuento
#para saber el precio final hacemos la operacion de resta ValorCompra menos el resultado del descuento 

print("la compra fue: ",ValorCompra, "el decuento final es: ",Descuento, "El precio final a pagar es: ",Preciofianl)
#imprimimos todo los resultados para que el usuario vea el precion final a pagar 
