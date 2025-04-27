def Ordenar(lista):
    if len(lista) < 2:
        return lista
    else:
        pivo = lista[0]
        maiores = []
        menores = []
    
        for i in range(1, len(lista)):
            if lista[i] <= pivo:
                menores.append(lista[i])
            else:
                maiores.append(lista[i])
    
        return(Ordenar(menores) + [pivo] + Ordenar(maiores))
    
minha_lista = [3, 5, 2, 1, 4]

print(Ordenar(minha_lista))