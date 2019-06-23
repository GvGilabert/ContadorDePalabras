import time
import platform
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()
print(filedialog.file)

class Ticker:
    def __init__(self,logData,tipodeproceso,nproceso):
        self.start_time = time.time()
        self.log=logData
        self.tipo=tipodeproceso
        self.n=nproceso

    # retorna delta tiempo en segundos
    def __call__(self):
        dt = time.time() - self.start_time
        self.start_time = time.time()
        file = open("log.csv","a")
        file.write(self.log + "," + self.tipo + "," + self.n + ","+ str(dt) )
        file.close

a = Ticker("cada","kakak","sdas")

a()
print(platform.system(),platform.version())

