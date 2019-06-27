import multiprocessing
from multiprocessing import Pool

RESULTADO = []
t = ['1','33','3']
class Resultado:
    Palabra=""
    Repeticiones=0




def Procesar2 (text):
    t = list(set(text))         #Copia de la lista de palabras sin duplicados
    e = []
    for i in t:                     #Recorre la lista sin duplicados (t)
        palabra = Resultado()       #Crea un nuevo objeto para almacenar el resultado
        palabra.Palabra = i         #Asigna la palabra actual a nuestro objeto de resultado
        for j in text:                  #Recorre la lista completa de palabras
            if (i==j):                      #Si encuentra una coincidencia
                palabra.Repeticiones += 1       #Suma uno al valor repeticiones de nuestro objeto resultado
        e.append(palabra) #Guardamos el resultado en una lista
    return e

text = t
oh =len(text)%4
tpt =len(text)//4
s = 0
f = oh + tpt
if __name__ == '__main__':
    pool = Pool(processes=4)
    p1 = pool.apply_async(Procesar2, (text[s:f]))
    s = f+1
    f += tpt
    p2 = pool.apply_async(Procesar2,(text[s:f]))
    s = f+1
    f += tpt
    p3 = pool.apply_async(Procesar2,(text[s:f]))
    s = f+1
    f += tpt
    p4 = pool.apply_async(Procesar2,(text[s:f]))
    pool.close();
    pool.join();
    RESULTADO.append(p1)
    RESULTADO.append(p2)
    RESULTADO.append(p3)
    RESULTADO.append(p4)

for i in RESULTADO:
    for j in i.get():
        print(j)