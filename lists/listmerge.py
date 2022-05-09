def juntar (lista1, lista2):
  nuevalista=[]
  x = 0 
  for i in range(len(lista1)):
    if (lista1[i] < lista2[i]):
      if (lista1[i] > x):
        x = lista1[i]
        nuevalista.append(lista1[i])
        x = lista2[i]
        nuevalista.append(lista2[i])
    elif (lista2[i]< lista1[i]):
      if (lista2[i] > x):
        x = lista2[i]
        nuevalista.append(lista2[i])
        x = lista1[i]
        nuevalista.append(lista1[i])
  return nuevalista