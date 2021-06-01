from tkinter import filedialog
from tkinter import *
import cv2 as cv
import tkinter


def openFile():
   
   filePath = filedialog.askopenfilename()
   global fileName
   fileName = str(filePath)

   print(filePath)
   readFile()

def readFile():
    
    imgread = cv.imread(fileName)
    cv.imshow("Photo", imgread)

def anamenu():
    screen = Tk()
    screen.geometry("400x200")
    screen.title("Resim Okuma")
    Label(screen, text="Resimleri Aç", font=("Calibri", 15)).pack()
    Label(screen, text="").pack()
    Label(screen, text="").pack()
    Label(screen, text="Açmak İstediğiniz Dosyayı Seçin", font=("Calibri", 15)).pack()
    Label(screen, text="").pack()
    secim = Button(screen, text="Aç", font=("Calibri", 15), command= openFile, fg="red", bg="black").pack()
    



    screen.mainloop()


#cv.imread()
anamenu()