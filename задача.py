import tkinter
import cv2 as cv
from tkinter import *
import tkinter.filedialog as fd
from PIL import Image, ImageTk


def choose_file(frame):
    filetypes = (("Изображение", "*.jpg *.gif *.png *.jpeg"),
                 ("Любой", "*"))
    filename = fd.askopenfilename(title="Открыть файл", initialdir="/users/lenovo/Desktop",
                                  filetypes=filetypes)
    image = tkinter.PhotoImage(file=filename)
    label = tkinter.Label(master=frame, image=image)
    return label


window = Tk()
window.title("Stitcher")
window.geometry("1080x720")
frame = tkinter.Frame(window)
#frame.grid()
frame0 = tkinter.Frame(master=window, height=360)
frame0.pack(fill=tkinter.BOTH, side=tkinter.BOTTOM, expand=True, anchor=CENTER)
frame_1 = tkinter.Frame(master=window, width=540, height=360, bg="green")
frame_1.pack(fill=tkinter.BOTH, side=tkinter.LEFT, expand=True)
frame2 = tkinter.Frame(master=window, width=540, bg="yellow")
frame2.pack(fill=tkinter.BOTH, side=tkinter.RIGHT, expand=True)
button = tkinter.Button(frame0, text="Button", command=choose_file)
button.place(relx=0.5, rely=0.5, anchor=CENTER)
img = tkinter.PhotoImage(lambda x:choose_file())
label0 = choose_file(frame0)
window.mainloop()


img_1 = cv.imread('1.jpg')
img_2 = cv.imread('2.jpg')
