import tkinter
import cv2
from tkinter import *
import tkinter.filedialog as fd
from PIL import Image, ImageTk

imgs_paths = []
images = {}


def choose_file1():
    filetypes = (("Изображение", "*.jpg *.gif *.png *.jpeg"),
                 ("Любой", "*"))
    filename = fd.askopenfilename(title="Открыть файл", initialdir="/users/lenovo/Desktop",
                                  filetypes=filetypes)
    images['filename1'] = filename
    img = ImageTk.PhotoImage(Image.open(filename))
    images['img1'] = img

    label1 = Label(frame1, image=images['img1'])
    label1.pack()


def choose_file2():
    filetypes = (("Изображение", "*.jpg *.gif *.png *.jpeg"),
                 ("Любой", "*"))
    filename = fd.askopenfilename(title="Открыть файл", initialdir="/users/lenovo/Desktop",
                                  filetypes=filetypes)
    images['filename2'] = filename
    img = ImageTk.PhotoImage(Image.open(filename))
    images['img2'] = img

    label2 = Label(frame2, image=images['img2'])
    label2.pack()


def stitcher():
    imgs = [cv2.imread(images['filename1']), cv2.imread(images['filename2'])]
    stitchy = cv2.Stitcher.create()
    (dummy, output) = stitchy.stitch(imgs)

    if dummy != cv2.STITCHER_OK:
        # checking if the stitching procedure is successful
        # .stitch() function returns a true value if stitching is
        # done successfully
        print("stitching ain't successful")
    else:
        print('Your Panorama is ready!!!')

    # final output
    cv2.imshow('final result', output)
    images['result'] = output
    cv2.imwrite('final result.jpg', output)
    #label0 = Label(frame0, image=output)
    #label0.pack()


window = Tk()
window.title("Stitcher")
window.geometry("1080x720")
frame0 = tkinter.Frame(master=window, height=360, borderwidth=1, relief=SUNKEN)
frame0.pack(fill=tkinter.BOTH, side=tkinter.BOTTOM, expand=True, anchor=CENTER)
frame1 = tkinter.Frame(master=window, width=540, height=360, borderwidth=1, relief=SUNKEN)
frame1.pack(fill=tkinter.BOTH, side=tkinter.LEFT, expand=True)
frame2 = tkinter.Frame(master=window, width=540, borderwidth=1, relief=SUNKEN)
frame2.pack(fill=tkinter.BOTH, side=tkinter.RIGHT, expand=True)

button1 = tkinter.Button(frame1, text="Выбрать файл", command=choose_file1)
button1.place(relx=0.5, rely=0.5, anchor=CENTER)
button2 = tkinter.Button(frame2, text="Выбрать файл", command=choose_file2)
button2.place(relx=0.5, rely=0.5, anchor=CENTER)
button0 = tkinter.Button(frame0, text="Сшить", command=stitcher)
button0.place(relx=0.5, rely=0.5, anchor=CENTER)
window.mainloop()
