
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
    texto = LeerTexto(archivo)
    return SetUp(texto, logData, process)

def LeerTexto(ARCHIVO):
    #Esta función debera leer un archivo txt con el nombre pasado por parametro desde el disco, quitarle todo lo que no sean palabras
    # (, . - _ : ; ! ? ...) e ingresarlos en una lista que devolverá en su return.
    texto = ["casa","casa","pasa","taza","etc"]
    print ("Cargando lista desde txt")
    return texto  

def SetUp(texto,logData,process):
    #Esta función en base a lo que le llegue por el parametro process, debe tomar la lista "texto" y la información de "logData" y
    #enviarla a la función que corresponda.
    #process 0: ProcesarSimple(texto,logData)
    #process 1: Solicitar por consola la cantidad de threads a utilizar y llamar a ProcesarThreads(texto,NdeThreads,logData)
    #process 2: Solicitar por consola la cantidad de procesos a utilizar y llamar a ProcesarProcesses(texto,NdeProcesses,logData)
    #process 3: Solicitar por consola la cantidad de procesos y sub threads a utilizar y llamar a ProcesarMixto(texto,NdeProcesses,NdeThreads,logData)
    if process == 0:
        return ProcesarSimple(texto,logData)
    elif process == 1:
        return ProcesarThreads(texto,hilos,logData)
    elif process == 2:
        return ProcesarProcesses(texto,hilos,logData)
    else:
        return ProcesarMixto(texto,hilos,subHilos,logData)

def Ticker(logData, tipoDeProceso, NrDeProcesos):
    #Función que inicia y finaliza un temporizador para llevar el control del tiempo que demoran en ejecutarse las diferentes formas de procesar 
    #la información. Además cada vez que finaliza un control de tiempo debe registrar en un archivo de texto la siguiente información separada por comas (csv):
    #logData,tipoDeProceso,NrDeProcesos,tiempoDemorado  
    # Esto sería: (Info de hardware, tipo de proceso (simple, thread, process), cantidad de hilos corridos, tiempo demorado)

def Procesar (text):
    #Función que recibe una lista de palabras, busca cuantas repeticiones hay de cada una y devuelve el resultado ordenado de mayor a menor de las 
    #repeticiones encontradas, Ej: {casa:102,papa:90,taza:36,etc...} Las puede devolver como una lista donde cada fila tenga un texto que sea 
    #palabra + cantidad de repeticiones (ordenada previamente), como una tupla que tenga nombre + cantidad o como un objeto del tipo resultado que 
    #tenga dos propiedades ej resultado{Palabra="casa",Repeticiones=102}
    return resultado = []

def ProcesarSimple(text,logData):
    #Inicia el Ticker(logData, "Simple", 1) para que inicie el control del tiempo.
    #Llama a Procesar(text)
    #Ejecutar Ticker() para controlar el tiempo demorado.
    return resultado = []

def ProcesarThreads(text,NdeThreads,logData):
    #Inicia el Ticker()
    #Divide la información de text por el NdeThreads y esa es la cantidad de palabras a procesar por thread.
    #Inicia un thread por cada NdeThreads y cada uno ejecuta Procesar(text) y le pasa por parametro una lista con la cantidad de palabras que le corresponda según 
    #el paso anterior.
    #Una vez que todos los threads terminaron (usar join para que espere a que todos terminen), unir todas las listas en una sola y devolver una sola únificada
    #y ordenada.
    #Ejecutar Ticker() para controlar el tiempo demorado.
    return resultado = []

def ProcesarProcesses(texto,NdeProcesses,logData):
    #Inicia el Ticker()
    #Divide la información de text por el NdeProcesses y esa es la cantidad de palabras a procesar por proceso.
    #Inicia un process por cada NdeProcesses y cada uno ejecuta Procesar(text) y le pasa por parametro una lista con la cantidad de palabras que le corresponda según 
    #el paso anterior.
    #Una vez que todos los process terminaron (usar join para que espere a que todos terminen), unir todas las listas en una sola y devolver una sola únificada
    #y ordenada.
    #Ejecutar Ticker() para controlar el tiempo demorado.
    return resultado = []

def ProcesarMixto(texto,NdeProcesses,NdeThreads,logData):
    #Inicia el Ticker()
    #Divide la información de text por el NdeProcesses y esa es la cantidad de palabras a procesar por proceso.
    #Inicia un process por cada NdeProcesses y cada uno ejecuta ProcesarThreads(text) y le pasa por parametro una lista con la cantidad de palabras que le corresponda según 
    #el paso anterior.
    #Una vez que todos los process terminaron (usar join para que espere a que todos terminen), unir todas las listas en una sola y devolver una sola únificada
    #y ordenada.
    #Ejecutar Ticker() para controlar el tiempo demorado.
    return resultado = []


#PROGRAMA PRINCIPAL
resultado = MenuDeOpciones()
#Acá se puede armar algo para que muestre x cantidad de resultados por pantalla o los guarde en un txt.




