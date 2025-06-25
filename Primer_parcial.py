from list_ import List
from queue_ import Queue
from stack_ import Stack
from super_heroes_data import superheroes

Lista_mia_superheroes = [ "Spiderman", "Iron Man", "Thor", "Hulk", "Black Widow", "Doctor Strange", "Wolverine", "Falcon", "Deadpool", "Black Panther","Hawkeye", "Vision", "Ant Man", "Scarlet Witch", "Capitan America" ]

def buscar_capitan(lista, indice=0):
    if indice >= len(lista):
        return False
    if lista[indice] == "Capitan America":
        return True
    return buscar_capitan(lista, indice + 1)


def listar_superheroes(lista, indice=0):
    if indice >= len(lista):
        return
    print(lista[indice])
    listar_superheroes(lista, indice + 1)

if buscar_capitan(Lista_mia_superheroes):
    print("Capitan America está en la lista.")
else:
    print("Capitan America no está en la lista.")

print("Listado de superhéroes:")
listar_superheroes(Lista_mia_superheroes)

def criterio_nombre(personaje):
    return personaje["name"]

lista = List()

for i in range(len(superheroes)):
    lista.append(superheroes[i])

lista.add_criterion("name", criterio_nombre)

lista.sort_by_criterion("name")

print("Listado ordenado por nombre:")
lista.show()

def criterio_nombre(personaje):
    return personaje["name"]

lista = List()
for i in range(len(superheroes)):
    lista.append(superheroes[i])

lista.add_criterion("name", criterio_nombre)
lista.sort_by_criterion("name")

pos_thing = lista.search("The Thing", "name")
pos_rocket = lista.search("Rocket Raccoon", "name")

print("The Thing está en la posición:", pos_thing)
print("Rocket Raccoon está en la posición:", pos_rocket)

lista = List()
for i in range(len(superheroes)):
    lista.append(superheroes[i])

print("Villanos en la lista:")
for i in range(len(lista)):
    personaje = lista[i]
    if personaje["is_villain"] == True:
        print(personaje["name"])


lista = List()
for i in range(len(superheroes)):
    lista.append(superheroes[i])

cola_villanos = Queue()

for i in range(len(lista)):
    personaje = lista[i]
    if personaje["is_villain"] == True:
        cola_villanos.arrive(personaje)

print("Villanos que aparecieron antes de 1980:")
cantidad = cola_villanos.size()
i = 0
while i < cantidad:
    villano = cola_villanos.attention()
    if villano["first_appearance"] < 1980:
        print(villano["name"], "-", villano["first_appearance"])
    i = i + 1

prefijos = ["Bl", "G", "My", "W"]
lista = List()
for i in range(len(superheroes)):
    lista.append(superheroes[i])

print("Superhéroes con Bl, G, My o W:")
for i in range(len(lista)):
    nombre = lista[i]["name"]
    coincide = False

    for j in range(len(prefijos)):
        if nombre.startswith(prefijos[j]):
            coincide = True

    if coincide:
        print(nombre)
        
def criterio_nombre_real(personaje):
    return personaje["real_name"]

lista = List()
for i in range(len(superheroes)):
    if superheroes[i]["real_name"] is not None:
        lista.append(superheroes[i])

lista.add_criterion("real_name", criterio_nombre_real)
lista.sort_by_criterion("real_name")

print("Listado ordenado por nombre real (ascendente):")
for i in range(len(lista)):
    personaje = lista[i]
    print(personaje["real_name"], "-", personaje["name"])

def criterio_aparicion(personaje):
    return personaje["first_appearance"]


lista = List()
for i in range(len(superheroes)):
    if superheroes[i]["is_villain"] == False:
        lista.append(superheroes[i])

lista.add_criterion("first_appearance", criterio_aparicion)
lista.sort_by_criterion("first_appearance")

print("Superhéroes ordenados por fecha de aparición:")
for i in range(len(lista)):
    personaje = lista[i]
    print(personaje["first_appearance"], "-", personaje["name"])

lista = List()
for i in range(len(superheroes)):
    lista.append(superheroes[i])

print("Nombre real de Ant Man a Scott Lang")
for i in range(len(lista)):
    if lista[i]["name"] == "Ant Man":
        lista[i]["real_name"] = "Scott Lang"

for i in range(len(lista)):
    if lista[i]["name"] == "Ant Man":
        print(lista[i])
    
lista = List()
for i in range(len(superheroes)):
    lista.append(superheroes[i])

print("Personajes con 'time-traveling' o 'suit' en su biografía:")
for i in range(len(lista)):
    bio = lista[i]["short_bio"]
    if "time-traveling" in bio or "suit" in bio:
        print(lista[i]["name"])
        print("Biografía:", bio)
    
lista = List()
for i in range(len(superheroes)):
    lista.append(superheroes[i])


def criterio_nombre(personaje):
    return personaje["name"]


lista.add_criterion("name", criterio_nombre)
lista.sort_by_criterion("name")


eliminado_electro = lista.delete_value("Electro", "name")
eliminado_zemo = lista.delete_value("Baron Zemo", "name")


if eliminado_electro is not None:
    print("Electro eliminado:")
    print(eliminado_electro)
else:
    print("Electro no estaba en la lista.")

if eliminado_zemo is not None:
    print("Baron Zemo eliminado:")
    print(eliminado_zemo)
else:
    print("Baron Zemo no estaba en la lista.")
