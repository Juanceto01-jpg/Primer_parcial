from list_ import List
from queue_ import Queue
from super_heroes_data import superheroes

Lista_de_superheroes_mia = ["Spiderman", "Capitan America", "Thor", "SuperMan", "Cat Woman", "Hulk", "Black Panther", "Pantera Negra", "Doctor Strange", "Punisher", "Ghost Rider", "Blade", "Deadpool", "Wolverine", "Batman"]

def buscar_capitan_recursivo(lista, objetivo, indice=0):
    if indice >= len(lista):
        return False
    if lista[indice] == objetivo:
        return True
    return buscar_capitan_recursivo(lista, objetivo, indice + 1)

def listarsuperheroes(lista, indice=0):
    if indice >= len(lista):
        return
    print(lista[indice])
    listarsuperheroes(lista, indice + 1)


def ordenar_por_nombre(personajes):
    print("Listado ordenado por nombre:")
    personajes_ordenados = sorted(personajes, key=lambda p: p["name"])
    for p in personajes_ordenados:
        print(p["name"])

def buscar_posiciones(personajes, nombre1, nombre2):
    lista = List()
    lista.extend(personajes)
    lista.add_criterion("name", lambda p: p["name"])
    lista.sort_by_criterion("name")
    pos1 = lista.search(nombre1, "name")
    pos2 = lista.search(nombre2, "name")
    print(f'"{nombre1}" está en la posición: {pos1}')
    print(f'"{nombre2}" está en la posición: {pos2}')

def listar_villanos(personajes):
    print("Villanos:")
    for p in personajes:
        if p["is_villain"]:
            print(p["name"])

def villanos_en_cola(personajes):
    colavillanos = Queue()
    for p in personajes:
        if p["is_villain"]:
            colavillanos.arrive(p)
    print("Villanos que aparecieron antes de 1980:")
    for _ in range(colavillanos.size()):
        villano = colavillanos.move_to_end()
        if villano["first_appearance"] < 1980:
            print(f"{villano['name']} ({villano['first_appearance']})")

def filtrar_por_prefijo(personajes, prefijos):
    print("\nSuperhéroes con iniciales", prefijos, ":")
    for p in personajes:
        if p["name"].startswith(prefijos) and not p["is_villain"]:
            print(p["name"])

def ordenar_por_real_name(personajes):
    lista = List()
    lista.extend(personajes)
    lista.add_criterion("real_name", lambda p: str(p["real_name"]))
    lista.sort_by_criterion("real_name")
    print("Listado por nombre real:")
    for p in lista:
        print(f"{p['real_name']} ({p['name']})")

def ordenar_heroes_por_aparicion(personajes):
    lista = List()
    lista.extend([p for p in personajes if not p["is_villain"]])
    lista.add_criterion("aparicion", lambda p: p["first_appearance"])
    lista.sort_by_criterion("aparicion")
    print("Superhéroes ordenados por aparición:")
    for p in lista:
        print(f"{p['name']} ({p['first_appearance']})")  

def modificar_antman(personajes):
    for p in personajes:
        if p["name"] == "Ant Man":
            p["real_name"] = "Scott Lang"
            print("Ant Man modificado a Scott Lang.")
            break

def personajes_por_biografia(personajes):
    print("Personajes con 'time-traveling' o 'suit' en su biografía:")
    for p in personajes:
        bio = p["short_bio"].lower()
        if "time-traveling" in bio or "suit" in bio:
            print(f"{p['name']}: {p['short_bio']}")  

def eliminar_personajes(personajes, nombres_a_eliminar):
    lista = List()
    lista.extend(personajes)
    lista.add_criterion("name", lambda p: p["name"])
    lista.sort_by_criterion("name")
    for nombre in nombres_a_eliminar:
        eliminado = lista.delete_value(nombre, "name")
        if eliminado:
            print(f"Se eliminó: {eliminado['name']}")
            print("Info:", eliminado)
        else:
            print(f"{nombre} no estaba en la lista.")


if buscar_capitan_recursivo(Lista_de_superheroes_mia, "Capitan America"):
    print("El capitan se encuentra en la lista")
else:
    print("No se encuentra en la lista")

listarsuperheroes(Lista_de_superheroes_mia)

ordenar_por_nombre(superheroes)
buscar_posiciones(superheroes, "The Thing", "Rocket Raccoon")
listar_villanos(superheroes)
villanos_en_cola(superheroes)
filtrar_por_prefijo(superheroes, ("Bl", "G", "My", "W"))
ordenar_por_real_name(superheroes)
ordenar_heroes_por_aparicion(superheroes)
modificar_antman(superheroes)
personajes_por_biografia(superheroes)
eliminar_personajes(superheroes, ["Electro", "Baron Zemo"])