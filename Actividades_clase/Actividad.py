#1 programa
palabra1=input("Ingrese la primera palabra")
palabra2=input("Ingrese la segunda palabra")
def imprimeUltimosTresCaracteres(palabraUno, palabraDos):
    print("Palabra uno termina en " + palabraUno[-3:])
    print("Palabra dos termina en " + palabraDos[-3:])
if palabra1[-3:]==palabra2[-3:]:
    print("Las palabras: " + palabra1 + " y " + palabra2)
    imprimeUltimosTresCaracteres(palabra1,palabra2)
else:
    print("Las palabras no riman")
    imprimeUltimosTresCaracteres(palabra1,palabra2)

#2 programa
class Persona:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
    def respirar (self):
        return ("Ya respire")
    def cumple (self):
        return "Estoy de cumple"
unaPersona=Persona("Doraemiton", 20)
print(unaPersona.nombre)
print(unaPersona.edad)
Persona2=Persona("Nobita", 19)
print(Persona2.nombre)
print(Persona2.edad)
Persona3=Persona("Doraemiton",20)
print(Persona3.nombre)
print(Persona3.edad)
Persona4=(unaPersona)
print(Persona4.nombre)
print(Persona4.edad)
unaPersona.nombre="Jarit"
unaPersona.edad=19

#3 programa
class Bombero (Persona):
    def trabaje (self):
        return ("Apague el incendio")
class Policia (Persona):
    def trabaje(self):
        return ("Atrape un delincuente")
Policia=Policia("Brihayan", 20)
print(Policia.nombre)
print(Policia.edad)
print(Policia.trabaje())
print(Policia.respirar())
policias=[]
unPolicia=Policia
policias.append(unPolicia)
policias.append(Policia)
for i in policias:
    print(i.nombre)
    print(i.edad)
