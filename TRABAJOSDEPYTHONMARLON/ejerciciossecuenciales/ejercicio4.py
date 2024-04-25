#comision de ventas
NombreVendedor= input("ingrese el nota del vendedor: ")
#declaramos la variable NombreVendedor con imput para redactar bien la compra
sueldo= float(input("ingrese el sueldo: "))
#decalramos la segunda variable para saber el sueldo base del vendedor 
PrimeraVenta= float(input("ingrese la primera venta: "))
#ingresamos la variable PrimeraVenta para la primera venta
SegundaVenta= float(input("ingrese la segunda venta: "))
#ingresamos la varibale segundaventa para la segunda compra
TercerVenta= float(input("ingrese la tercer venta: "))
#ingresamos la variable TercerVenta la tercera compra
comision=(PrimeraVenta+SegundaVenta+TercerVenta) * .15
#ingresamos la comision y hacemos la suma de todas las ventas y lo multiplicamos por el porcentaje de comision de la venta
print("el nombre del vendedor es: ",NombreVendedor, "el sueldo del vendedor es: ",sueldo, "la comision de la quincena pro la 3 ventas es: ",comision, "el sueldo de la comision es :",sueldo+comision )
#imprimimos todos los datos que hemos pedido para terminar la comision que gana el vendedor por la quincena