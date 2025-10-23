#Clase 4 de la semana 4 (de la segunda que fue grabada type shi)

unc = 41        #valor entero
mango = 67.4167     #valor flotante chaval
usuario = "Harry"
barber_shop_cost = 0.25
matcha = -6921.6741

print(type(unc))
print(type(mango))

print(type(unc) is int) #no es lo mismo que escribir "int" ya que eso es una palabra nomas
print(type(mango) is int)

print("el good boy es",usuario,"y tiene",mango,"niche labubus")
print("y tiene", unc, "niños en su sotano")

#hermano el f string como el silent hill f famoso videojuego que salio este año (2025)

print(f"el bad boy es {usuario}")

"""
Basicamente los f strings te dejan usar variables en las propias "" lo cual a simple vista
no parece muy meta pero esta bastante cheto y btw siempre se activa si usas las {} pq sino
no cuela
"""

print(f"y tiene {mango - 10 + 10 - 26:.3f} niche labubus") #se pueden hacer sumas y todo eso btw
print(f"y con todos sus brain rots robados consigue {unc + mango + barber_shop_cost * mango:.2f} gancillones por micronanomacro segundos")

"""
Como se puede ver en este niche ejemplo en las lineas 27 y 28 se usa algo muy niche el cuales
son las combinaciones de las f strings por lo que tengo entendido las cuales son

:.2f >>> que bueno tengo entendido que el punto es para determinar como decimales y el numero
        que va despues es para indicar cuantos decimales quieres que spawneen despues del
        puntico, los dos puntos al principio me imagino que son los que comienzan el combo
        so
"""
print(f"y el aura perdidad fue de ${abs(matcha):,.2f} aura points")

"""
        Lo que entendi del comando [abs] es que transforma cualquier numero con signos a un numero
sin signos por ejemplo tengo un -5 pues con abs lo va transformar en un 5 normal, tengo entendido
que es como lo mismo que en la calcu y tal 

Oh y mencionar que la coma que esta en :,.2f es para que ponga una coma en el primer numero ig
"""

print(type(usuario) is str)

labubu_phonk = True #OJO cahval que tienen que ir con mayuscula el True y False
print(type(labubu_phonk) is bool)

"""
Bueno el teacer no lo explica pero luego hay unos codigos que van asi 
or      x or y          Either x or y is True
and     x and y         Both x and y are True
not     not x           x is not True
"""

nombr3 = "Pancho"
ap3llido = "7w7"
nombr3_compl3to = nombr3 + ap3llido

print(nombr3_compl3to)
#puede dar erro si se intenta printear variables de texto con las de numeros