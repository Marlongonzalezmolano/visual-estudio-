#ejericicio de algoritmia del estudiante 
print("ingrese las notas del 1 al 100") #aca hacemos de que el programa imprima un eneucniado de que solo el profesor ingrese un numero del 1 al 100
primeracalificacion = int(input("ingrese la primera calificacion :")) # aca desclarmaos la primera clasificacion y hacemos de que ingrese la primera califiacion 
segundacalificacion = int(input("ingrese la segunda calificacion :")) #aca desclarmaos la segunda clasificacion y hacemos de que ingrese la segunda califiacion 
terceracalificacion = int(input("ingrese la tercera calificacion :")) #aca desclarmaos la tercera clasificacion y hacemos de que ingrese la tercera califiacion 

Promedio=(primeracalificacion+segundacalificacion+terceracalificacion)/3 # declaramos la varibale promedio y de ahi hacemos la suma de todas las notas ingresadas y a eso lo dividimos por 3

print("el promedio es", Promedio) # impirmimos el siguiente comentario con el resultado 

if Promedio>=70: # ponemos las siguiente condicion si el promedio es mayot o igual a 70 nos dirigira al siguiete camino
 print("aprueba la materia del algoritmia") # que imprima la materia de algoritmia a sido a provada 
else: # con el else hacemos de que coja otra condicion y que si no es correcto 
 print("reprueba algoritmia") # imprima reprueba algoritmia 
 
 
 



