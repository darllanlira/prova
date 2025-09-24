def selectionSort(addlista):
    n = len(addlista)
    for i in range(n):
        
        indice_maximo = i
        for j in range(i + 1, n):
            if addlista[j] > addlista[indice_maximo]:
                indice_maximo = j
        if indice_maximo != i:
            addlista[i], addlista[indice_maximo] = addlista[indice_maximo], addlista[i]
    
    return addlista
addlista=[8,6,5,0,3,4]

print(selectionSort(addlista))
      