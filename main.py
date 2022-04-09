##importamos la clase
from clases.Personaje import Personaje

##creando variable 
personaje= Personaje("juan", 800)
# personaje.nombre="Andres"-- al pasar los parametos al contructor no es necesaria esta inea 
# personaje.edad=800

##accsediendiendo a los metodos seter 
personaje.nombre="katalina"
personaje.edad=-30

#Acesediednto a los metodos geter 
print(personaje.nombre)
print(personaje.edad)