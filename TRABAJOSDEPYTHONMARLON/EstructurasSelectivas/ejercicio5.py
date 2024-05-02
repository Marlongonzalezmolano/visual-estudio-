# calculo de pulsaciones 
sexo=str(input("ingrese el sexo: ")) # primero declaro la varible de sexo para que el usuario lo ingrese
edad=int(input("ingrese la edad: ")) # declaro la vairiable de edad para que el usuario la ingrese 

if sexo == "femenino": #despues utilizo un condicional para que si el sexo es femenino dire al siguiente proceso 
    num_Pulsaciones = (220-edad)/10 # declaro numero de pulsaciones y hacemos la siguiente operacion que es 220- edad divido en 10 para la persona femenina
    print("Su numero de pulsaciones es: ",num_Pulsaciones) #imprimimos el numero de pulsaciones de acuerdo con lo que el usuario ha ingresado 

elif sexo == "masculino": # utilizamos la el condicional elif para declarar de que si sexo es igual a masculino pueda dirigir a lo sigueinte:
    num_Pulsaciones2 = (210-edad)/10 #declaro el numero de pulsacion 2 para que se haga la siguiente operacion 210 restado por la edad del usuario y esto lo dividimos en 2
    print("Su numero de pulsaciones es: ",num_Pulsaciones2) #hacemos de que se imprima de acuerdo a lo que el usuario ha colocado 
else:
    print("el sexo no es valido") # por ultimo utilizo el condicional else que es si no se cumple ponga un comentrario de que el sexo no es valido 


     


