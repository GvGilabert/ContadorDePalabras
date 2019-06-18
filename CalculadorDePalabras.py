
#Este es un programa que debe leer un archivo TXT y devolver un listado de las palabras que aparecen en el mismo
#y cuantas veces aparece cada una. Además debera dejar un log en un archivo de texto del tiempo demorado y en que
# hardware y SO se ejecutó para poder llevar estadisticas. 
#
#El programa tiene que poder correrse de tres formas diferente:
# - En un solo hilo de ejecución, corriendo la función de forma tradicional
# - Utilizando threads, pudiendo especificar la cantidad a utilizar 
# - Utilizando processes, pudiendo especificar la cantidad a utilizar
#
#ESTRUCTURA DEL PROGRAMA

def MenuDeOpciones():
    #En esta función se debera pedir por consola al usuario que ejecuta el programa que ingrese
    #los siguientes datos:
    # 
    # HARDWARE (Un texto describiendo el hardware donde se correrá el programa, cpu y cantidad de memoria)
    # SISTEMA_OPERATIVO (El sistema operativo donde se correrá el programa)
    # ARCHIVO (Nombre del archivo a procesar, se debera aclarar que el mismo tiene que estar en la misma carpeta que el programa)
    # FORMA_DE_PROCESAR (Se debera pedir que ingrese un número para definir la forma de procesar el archivo,
    #                      0 - NORMAL EN UN SOLO THREAD Y UN SOLO HILO
    #                      1 - MULTI THREAD
    #                      2 - MULTI PROCESOS
    #                      3 - MIXTO (PROCESOS QUE CORREN N CANTIDAD DE THREADS ADENTRO))
    #
    #EXTRAS: - Invesitagar si se pueden tomar los datos de hardware y SO directamente de la máquina en vez de solicitarlos por consola
    archivo = "unTexto.txt" 
    logData = HARDWARE + " " + SISTEMA_OPERATIVO
    process = 1

    texto = LeerTexto(archivo)
    SetUp(texto, logData, process)
    
    print("menu")

def LeerTexto(ARCHIVO):
    #Esta función debera leer un archivo txt con el nombre pasado por parametro desde el disco, quitarle todo lo que no sean palabras
    # (, . - _ : ; ! ? ...) e ingresarlos en una lista que devolverá en su return.
    lista = ["casa","casa","pasa","taza","etc"]
    print ("Cargando lista desde txt")
    return lista   

def SetUp(texto,logData,process):
    #Esta función en base a lo que le llegue por el parametro process, debe tomar la lista "texto" y la información de "logData" y
    #enviarla a la función que corresponda.
    #process 0: Procesar(texto,logData)
    #process 1: Solicitar por consola la cantidad de threads a utilizar y llamar a ProcesarThreads(texto,NdeThreads,logData)
    #process 2: Solicitar por consola la cantidad de procesos a utilizar y llamar a ProcesarProcesses(texto,NdeProcesses,logData)
    #process 3: Solicitar por consola la cantidad de procesos y sub threads a utilizar y llamar a ProcesarMixto(texto,NdeProcesses,NdeThreads,logData)


lista = LeerTexto(ARCHIVO)




