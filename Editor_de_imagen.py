#importamos las siguientes liberias 
from tkinter import *
from tkinter  import filedialog
import cv2
import numpy as np 
#Aqui llamamos  a la pantalla y sus diferentes atributos 
pnt = Tk()
pnt.geometry("390x300")
pnt.title("BUSCADOR")
pnt.resizable(False,False)
#Agregamos un try except  para el programa 
try:
#en este def abrirmos el buscador de la imagen a modificar 
    def Abrir():
        global archivo 
#Dentro de la variable archivo debemos de cambir el nombre de /home por   la raiz de busqueda en mi caso como uso linux es / home en caso de windows es poner la ruta donde se quiere iniciar  la busqueda
        archivo = filedialog.askopenfilename(title="abrir",initialdir="/home",filetypes=(("Todos los archivos","*.*"),("fotografia","*.png*")))
        print(archivo)
        pnt.quit()
        open = imagen()
#En este def se abre despues de seleccioanr un archivo y editar la imagen
    def imagen():
        def nothing(a):
            pass
        cv2.namedWindow('Tester')
        cv2.createTrackbar('HH','Tester',0,179,nothing)
        cv2.createTrackbar('HL','Tester',0,179,nothing)
        cv2.createTrackbar('SH','Tester',0,255,nothing)
        cv2.createTrackbar('SL','Tester',0,255,nothing)
        cv2.createTrackbar('VH','Tester',0,255,nothing)
        cv2.createTrackbar('VL','Tester',0,255,nothing)
        img = cv2.imread(archivo)
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) 
        key = cv2.waitKey(1)
        while not key == ord('q'):
            hh = cv2.getTrackbarPos('HH','Tester')
            hl = cv2.getTrackbarPos('HL','Tester')
            sh = cv2.getTrackbarPos('SH','Tester')
            sl = cv2.getTrackbarPos('SL','Tester')
            vh = cv2.getTrackbarPos('VH','Tester')
            vl = cv2.getTrackbarPos('VL','Tester')
            lower_white = np.array([hl,sl,vl], dtype=np.uint8)
            upper_white = np.array([hh,sh,vh], dtype=np.uint8)
            mask = cv2.inRange(hsv, lower_white, upper_white)
            cv2.imshow("BLACK AND WITHE", mask)
            cv2.imshow("IMAGE", img)
            key = cv2.waitKey(1)
except:
    print("Error")
    sys.exit()
#aqui generamos el boton para abrir el def llamado abrir y ejecutar el programa
Button(pnt,text="Seleccionar archivo",command=Abrir).grid(row=1,column=0,padx=70,pady=125)
Label(pnt,text="PARA SALIR  DE LAS SIGUIENTES VENTANAS PRESIONE   "+"'Q'").grid(row=2,column=0,padx=0,pady=0)
cv2.destroyAllWindows()
pnt.mainloop()
