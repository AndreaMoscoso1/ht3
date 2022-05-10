##BUSQUEDA BINARIA
def binary_search (lista,search):
  principio = 0
  final =  len(lista)-1
  while principio<= final:
    mitad = (principio + final)//2
    if lista[mitad] == search:
      return "Si hay"
    elif lista [mitad] < search:
      principio = mitad + 1
    elif lista[mitad] > search:
      final = mitad - 1
  return "no hay"

print(binary_search(list,2))