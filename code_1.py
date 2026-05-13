class Animal:
    def hablar(self):
     print ("Este animal emite un sonido")

class Perro(Animal):
    def ladrar(self):
     print ("Guau Guau")

class gato(Animal):
    def maullar(self):
     print ("miau miau")

mi_perro= Perro ()
mi_perro.hablar()
mi_perro.ladrar()

mi_gato= gato ()
mi_gato.hablar()
mi_gato.maullar()

Animal = input("Escribe Perro o gato")

if Animal== Perro:
    print("Este animal dice Guau Guau")
else:
    print("Este animal dice miau miau")