from msilib.schema import Class
from tkinter.messagebox import NO


class Personaje:
    ##constructor 
    def __init__(self, name, age):
        ##atributos
        self.__nombre=name  ##el guion bajo _nombre equivale a que es un dato protegido 
        self.__edad=age      ##para hacer que un dato se vuelva provado se ingresa en el contriucctor con dos guines bajos 

### todos los atributos de una clase deben ser privados y los metodos deben ser publicos 

###metodos GET (obtener el valor del atributo )sirve para leer un atributo , GET es una funcion-... todos los metodos de las clases en ppython llevan el self 
    @property #para escribir una anotacion se hace con una @, De esta manera se concierte en el metodo GET
    def nombre(self):
        return self.__nombre
    
    @property 
    def edad (self):
        return self.__edad


###metodos SET (SIRVE PARA ESCRIBIR O LLEVAR UN VALOR A UN ATRIBUTO) este no retorna nada y solo asigna el valor, recibe el parametro dentro de la funcion de lo que yo quiero asinar
    
    @nombre.setter ##en este caso el decorador para aceder a la propiedad se ingresa con el mismo nombre del atributosmas el .setter .. en esta area validamos los datos 
    def nombre(self,nombre):
        self.__nombre=nombre 
    
    @edad.setter ##en este caso el decorador para aceder a la propiedad se ingresa con el mismo nombre del atributosmas el .setter  
    def edad(self,edad):
        if (edad<=0):
            print("no acepto edades negativas")
        else:
            self.__edad=edad
     
    