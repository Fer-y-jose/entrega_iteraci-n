def anadir_pal(pal_nueva, palabras):
    pal_ant = None
    pal_desp = None
    ind_ant = None
    ind_desp = None
    
    for idx, palabra in enumerate(palabras):
        if pal_nueva < palabra[0]:
            #encima de la pal nueva
            if pal_desp is None or pal_desp > palabra[0]:
                pal_desp = palabra[0]
                ind_desp = idx
        else:
            #debajo de la pal nueva
            if pal_ant is None or pal_ant < palabra[0]:
                pal_ant = palabra[0]
                ind_ant = idx
                
    if ind_ant is not None:
        temp = list(palabras[ind_ant])
        temp[2] = len(palabras) + 1
        palabras[ind_ant] = tuple(temp)
    if ind_desp is not None:
        temp = list(palabras[ind_desp])
        temp[1] = len(palabras) + 1
        palabras[ind_desp] = tuple(temp)
        
    pal_nuev_comp = [            
        pal_nueva,
        ind_ant + 1 if ind_ant is not None else 0,
        ind_desp + 1 if ind_desp is not None else -1
    ] 
    pal_nuev_comp = tuple(pal_nuev_comp)
    
    palabras.append(pal_nuev_comp)   
palabras = [
    ("avion", 3, 4),
    ("tren", 4, -1),
    ("auto", 0, 1),
    ("camion", 1, 2)
]
pal_nueva = input("Escriba una nueva palabra: ")
anadir_pal(pal_nueva, palabras)

print(palabras)

def eliminar_pal(pal_elim, palabras):
    idx_elim = 0
    while idx_elim < len(palabras) and palabras[idx_elim][0] != pal_elim:
        idx_elim += 1
       
    num_izq = palabras[idx_elim][1]
    num_dcha = palabras[idx_elim][2]
 
    if num_izq != 0:
        temp = list(palabras[num_izq - 1])
        temp[2] = num_dcha
        palabras[num_izq - 1] = tuple(temp)
        
    if num_dcha != -1:
        temp = list(palabras[num_dcha - 1])
        temp[1] = num_izq
        palabras[num_dcha - 1] = tuple(temp)
        
    _ = palabras.pop(idx_elim) 
    
    idx_elim += 1
    for idx, palabra in enumerate(palabras):
        temp = list(palabra)
        if temp[1] > idx_elim:
            temp[1] -= 1
        if temp[2] > idx_elim:
            temp[2] -= 1
        palabra = tuple(temp)
        palabras[idx] = palabra

pal_elim = input("escriba la palabra que desee eliminar: ")

eliminar_pal(pal_elim, palabras)

print(palabras)
