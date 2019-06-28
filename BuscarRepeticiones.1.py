#Este es un programa que debe leer un archivo TXT y devolver un listado de las palabras que aparecen en el mismo
#y cuantas veces aparece cada una. Además debera dejar un log en un archivo de texto del tiempo demorado y en que
# hardware y SO se ejecutó para poder llevar estadisticas. 
#
#El programa tiene que poder correrse de tres formas diferente:
# - En un solo hilo de ejecución, corriendo la función de forma tradicional
# - Utilizando threads, pudiendo especificar la cantidad a utilizar 
#
#ESTRUCTURA DEL PROGRAMA

#IMPORTS
import time
import platform
import tkinter as tk
from tkinter import filedialog
import threading
from multiprocessing import Pool
import cpuinfo
import psutil
import multiprocessing 

RESULTADO = [] #Lista donde se guardaran los resultados
    
#Ticker
#Clase que inicia y finaliza un temporizador para llevar el control del tiempo que demoran en ejecutarse las diferentes formas de procesar 
#la información. Además cada vez que finaliza un control de tiempo debe registrar en un archivo de texto la siguiente información separada por comas (csv):
#logData,tipoDeProceso,NrDeProcesos,tiempoDemorado  
# Esto sería: (Info de hardware, tipo de proceso (simple, thread, process), cantidad de hilos corridos, tiempo demorado)
class Ticker:
    def __init__(self,id,logData,tipodeproceso,nproceso):
        self.start_time = time.time()
        self.log=logData
        self.tipo=tipodeproceso
        self.n=nproceso
        self.i=id

    # retorna delta tiempo en segundos
    def __call__(self):
        dt = time.time() - self.start_time
        self.start_time = time.time()
        file = open("LOG_PALABRAS.csv","a")
        file.write(self.i+","+self.log + "," + self.tipo + "," + self.n + ","+ str(dt) +"\n" )
        file.close

#Resultado, una clase simple solo para poder guardar en una lista juntos la palabra y su cantidad de repeticiones
class Resultado:
    Palabra=""
    Repeticiones=0


#def MenuDeOpciones():
    #En esta función se debera pedir por consola al usuario que ejecuta el programa que ingrese
    #los siguientes datos:
    # 
    # HARDWARE (Un texto describiendo el hardware donde se correrá el programa, cpu y cantidad de memoria)
    # SISTEMA_OPERATIVO (El sistema operativo donde se correrá el programa)
    # ARCHIVO (Nombre del archivo a procesar, se debera aclarar que el mismo tiene que estar en la misma carpeta que el programa)
    # FORMA_DE_PROCESAR (Se debera pedir que ingrese un número para definir la forma de procesar el archivo,
    #                      0 - NORMAL EN UN SOLO THREAD Y UN SOLO HILO
    #                      1 - MULTI THREAD
    #
    #EXTRAS: - Invesitagar si se pueden tomar los datos de hardware y SO directamente de la máquina en vez de solicitarlos por consola
    
    # texto = LeerTexto(archivo)
    #return SetUp(texto, logData, process)
def MenuDeOpciones(): 
    so = platform.system(),platform.version()
    procesador = cpuinfo.get_cpu_info()['brand']
    nucleos = psutil.cpu_count()
    ram = format(psutil.virtual_memory()[0] / 2**30, '.2f') + "GBs"
    hardware = procesador + "de "+ str(nucleos) + " RAM:"+ram
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt")])
    texto = LeerTexto(file_path)
    logData = hardware+","+" ".join(so)

    process = int(input("Ingrese el tipo de proceso que desea realizar \n    0 - NORMAL EN UN SOLO THREAD Y UN SOLO HILO \n    1 - MULTI THREAD \n"))
    while process < 0 or process > 1:
        print("ERROR, opción invalida")
        process = int(input("Ingrese el tipo de proceso que desea realizar \n    0 - NORMAL EN UN SOLO THREAD Y UN SOLO HILO \n    1 - MULTI THREAD\n"))

    return SetUp(texto,logData,process)


#def LeerText()
#Esta función debera leer un archivo txt con el nombre pasado por parametro desde el disco, quitarle todo lo que no sean palabras
# (, . - _ : ; ! ? ...) e ingresarlos en una lista que devolverá en su return.
def LeerTexto(ARCHIVO):
    texto = []
    delete_list = ['\n',',', '.','!', '¡', '?', '¿', '[', ']', '(', ')', '_', '-',';', ':','0','1','2','3','4','5','6','7','8','9','10']
    fileIn = open(ARCHIVO, mode=('rt'), encoding=('utf-8'))
    for line in fileIn:
        for word in delete_list:
            line = line.replace(word,"")
            
        for word2 in line.split():
            texto.append(word2)
    fileIn.close()
    print ("Palabras a procesar: "+str(len(texto)))
    return texto

#def SetUp(texto,logData,process):
    #Esta función en base a lo que le llegue por el parametro process, debe tomar la lista "texto" y la información de "logData" y
    #enviarla a la función que corresponda.
    #process 0: ProcesarSimple(texto,logData)
    #process 1: Solicitar por consola la cantidad de threads a utilizar y llamar a ProcesarThreads(texto,NdeThreads,logData)
    #process 2: Solicitar por consola la cantidad de procesos a utilizar y llamar a ProcesarProcesses(texto,NdeProcesses,logData)
    #process 3: Solicitar por consola la cantidad de procesos y sub threads a utilizar y llamar a ProcesarMixto(texto,NdeProcesses,NdeThreads,logData)
def SetUp(texto,logData,process):
    sinReps = list(set(texto)) 
    if process == 0:
        return ProcesarSimple(sinReps,texto,logData)
    elif process == 1:
        hilos = int(input("Ingrese cantidad de threads a utilizar: "))
        MultiProccesing(sinReps,texto,hilos,logData)

# def PROCESAR
#Función que recibe una lista de palabras, busca cuantas repeticiones hay de cada una y devuelve el resultado ordenado de mayor a menor de las 
#repeticiones encontradas, Ej: {casa:102,papa:90,taza:36,etc...} Las puede devolver como una lista donde cada fila tenga un texto que sea 
#palabra + cantidad de repeticiones (ordenada previamente), como una tupla que tenga nombre + cantidad o como un objeto del tipo resultado que 
#tenga dos propiedades ej resultado{Palabra="casa",Repeticiones=102}
def Procesar (sre,id,text,log,tipo,hilos):
    timer = Ticker(id,log,tipo,str(hilos))
    t = sre        #Copia de la lista de palabras sin duplicados
    e = []
    for i in t:                     #Recorre la lista sin duplicados (t)
        palabra = Resultado()       #Crea un nuevo objeto para almacenar el resultado
        palabra.Palabra = i         #Asigna la palabra actual a nuestro objeto de resultado
        for j in text:                  #Recorre la lista completa de palabras
            if (i==j):                      #Si encuentra una coincidencia
                palabra.Repeticiones += 1       #Suma uno al valor repeticiones de nuestro objeto resultado
        e.append(palabra) #Guardamos el resultado en una lista
    timer()
    return e

#def PROCESARSIMPLE
#     #Inicia el Ticker(logData, "Simple", 1) para que inicie el control del tiempo.
#     #Llama a Procesar(text)
#     #Ejecutar Ticker() para controlar el tiempo demorado.
#     return resultado = []
def ProcesarSimple(sre,text,logData):
    r = Procesar(sre,"1",text,logData,"Simple",1)
    r.sort(key=lambda x: x.Palabra, reverse=True)
    return r


# def ProcesarThreads(text,NdeThreads,logData):
#     #Inicia el Ticker()
#     #Divide la información de text por el NdeThreads y esa es la cantidad de palabras a procesar por thread.
#     #Inicia un thread por cada NdeThreads y cada uno ejecuta Procesar(text) y le pasa por parametro una lista con la cantidad de palabras que le corresponda según 
#     #el paso anterior.
#     #Una vez que todos los threads terminaron (usar join para que espere a que todos terminen), unir todas las listas en una sola y devolver una sola únificada
#     #y ordenada.
#     #Ejecutar Ticker() para controlar el tiempo demorado.
#     return resultado = []
def ProcesarThreads(sre, text,NdeThreads,logData):
    m = NdeThreads
    oh=len(text)%NdeThreads
    tpt=len(text)//NdeThreads
    s = 0
    f = oh + tpt
    threads = []
    from multiprocessing.pool import ThreadPool
    pool = ThreadPool(processes=NdeThreads)

    while NdeThreads>0:
        partText = text[s:f]
        threads.append(pool.apply_async(Procesar, (sre,str(NdeThreads)+"/"+str(m), partText,logData,"Threads",str(NdeThreads))))
        s = f+1
        f += tpt
        NdeThreads -= 1
    for i in threads:
        for j in i.get():
            RESULTADO.append(j)

def MultiProccesing(sre, text,NdeThreads,logData):
    m = NdeThreads
    oh=len(text)%NdeThreads
    tpt=len(text)//NdeThreads
    s = 0
    f = oh + tpt
    if __name__ == '__main__': 
        with multiprocessing.Manager() as manager: 
            while NdeThreads>0:
                partText = text[s:f]
                p = multiprocessing.Process(target=Procesar, args=(sre,str(NdeThreads)+"/"+str(m), partText,logData,"Threads",str(NdeThreads)))
                p.start()
                p.join()
                s = f+1
                f += tpt
                NdeThreads -= 1



#PROGRAMA PRINCIPAL
var = MenuDeOpciones()
count = 0
if RESULTADO is not None:
    RESULTADO.sort(key=lambda x: x.Palabra, reverse=True)
    for j in RESULTADO:
        print(j.Palabra,j.Repeticiones)
        count +=1

if var is not None:
    for i in var:
        print(i.Palabra,i.Repeticiones)
        count +=1