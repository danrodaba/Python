'''
Escribir una función que calcule el máximo común divisor de dos números y otra que calcule el mínimo común múltiplo.
'''
def MCM_MCD(a,b):
    def divisores(n):
        a = 1
        lista=[]
        while a != n:
            a += 1
            if n % a == 0:
                lista.append(a)
                n=n/a
                a=1
        return lista
    def indices(lista):
        indice=[]
        for i in lista:
            if i not in indice:
                indice.append(i)
            else:
                continue
        return indice
    def contador(indice, lista):
        n_veces = []
        for i in indice:
            a=lista.count(i)
            n_veces.append(a)
        diccionario=dict(zip(indice,n_veces))
        return diccionario
    div_a = divisores(a)
    div_b = divisores(b)

    ind_a=indices(div_a)
    ind_b=indices(div_b)

    dict_a=contador(ind_a,div_a)
    dict_b=contador(ind_b,div_b)
    comunes={}

    for x1,y1 in dict_a.items():
        for x2,y2 in dict_b.items():
            if x1==x2:
                comunes[x1]=min(y1,y2)
    MCD=1

    for x,y in comunes.items():
        MCD*=x**y

    dict_final={}

    for i in dict_a:
        if i in dict_b:
            dict_final[i]=max(dict_a[i],dict_b[i])
        else:
            dict_final[i]=dict_a[i]
    for i in dict_b:
        if i not in dict_final:
            dict_final[i]=dict_b[i]

    MCM=1
    for x,y in dict_final.items():
        MCM*=x**y
    print('MCM:', MCM, ' MCD: ',MCD)
    return [MCM, MCD]

print(MCM_MCD(40,16))