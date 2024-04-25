#perimetro y area de un rectangulo

base= int(input("ingrese la base del rectagulo: "))
#declaro la primer variable base con int para que deje ingresar caracteres numericos 
altura= int(input("ingrese la altura del rectangulo: "))
#declaro la sugunda variable con int para que ingrese el caracter numerico 
perimetro=base*2+altura*2
#primero para hallar el perimetro tengo base x 2 y altura x 2 para que me bote el perimte
area= (base*altura)
#para hallar area toca multiplicar la base por la altura
print("el perimetro del rectangulo es: ",perimetro,"el area del de rectangulo",area) 
#por utlimo utilizamos el print para que bote toda la informacion al usuario 
