#nota final de un algortmo estudiante 
NombreEstudiante= input("ingrese el nomrbre del Estudiante: ")
#primera variable nombre del estudiante para que el ingrese su nombre
CalificacionActividades= float(input("ingrese la califiacion de la actividad: "))
#Declaramos la variable de CalificacionActividades para ingresar la primera nota
Proyectofinal= float(input("ingrese la calificacion del proyecto final: "))
#Declaramos la variable de CalificacionActividades para ingresar la nota correspondida
EvaluacionParcial= float(input("ingrese la calificacion de la evaluacion parcial: "))
#Declaramos como EvaluacionParcial para que ingresen la calificaicon de esta

CalificacionFinal= (CalificacionActividades*0.3)+(Proyectofinal*0.5)+(EvaluacionParcial*0.2)
#para hallar clasificacionfinal devemos multiplicar calificacionActividades por el porcentaje y sumamos con la siguiente calificacion Proyectofinal lo multiplicamos por porcentaje y sumamos la ultima nota por la evaluacion parcialpor el porcentaje y hacemos la suma completo  
print("La nota final es: ",CalificacionFinal)